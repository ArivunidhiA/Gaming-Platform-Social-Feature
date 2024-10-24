import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import json

class GamingSocialPlatform:
    def __init__(self):
        # Load sample data
        self.users = pd.read_csv('data/users.csv')
        self.gaming_history = pd.read_csv('data/gaming_history.csv')
        self.friend_connections = pd.read_csv('data/friend_connections.csv')
        
    def create_user_profile(self, user_id, username, favorite_genres, playtime_hours=0):
        """Create a new user profile"""
        new_user = {
            'user_id': user_id,
            'username': username,
            'favorite_genres': favorite_genres,
            'playtime_hours': playtime_hours,
            'join_date': datetime.now().strftime('%Y-%m-%d')
        }
        self.users = pd.concat([self.users, pd.DataFrame([new_user])], ignore_index=True)
        return new_user

    def update_gaming_history(self, user_id, game_id, hours_played):
        """Update gaming history for a user"""
        new_history = {
            'user_id': user_id,
            'game_id': game_id,
            'hours_played': hours_played,
            'last_played': datetime.now().strftime('%Y-%m-%d')
        }
        self.gaming_history = pd.concat([self.gaming_history, pd.DataFrame([new_history])], 
                                      ignore_index=True)

    def get_friend_recommendations(self, user_id, n_recommendations=5):
        """Generate friend recommendations based on gaming similarity"""
        # Get user's gaming history
        user_history = self.gaming_history[self.gaming_history['user_id'] == user_id]
        
        if user_history.empty:
            return "No gaming history found for this user."
        
        # Create user-game matrix
        user_game_matrix = self.gaming_history.pivot_table(
            index='user_id', 
            columns='game_id', 
            values='hours_played',
            fill_value=0
        )
        
        # Calculate similarity between users
        user_similarity = cosine_similarity(user_game_matrix)
        user_similarity_df = pd.DataFrame(
            user_similarity,
            index=user_game_matrix.index,
            columns=user_game_matrix.index
        )
        
        # Get existing friends
        existing_friends = self.friend_connections[
            (self.friend_connections['user_id_1'] == user_id) |
            (self.friend_connections['user_id_2'] == user_id)
        ]
        existing_friends_ids = existing_friends['user_id_1'].tolist() + \
                             existing_friends['user_id_2'].tolist()
        
        # Get recommendations
        user_similarities = user_similarity_df.loc[user_id]
        recommendations = user_similarities.sort_values(ascending=False)[1:]  # Exclude self
        
        # Filter out existing friends
        recommendations = recommendations[~recommendations.index.isin(existing_friends_ids)]
        
        # Get top N recommendations
        top_recommendations = recommendations.head(n_recommendations)
        
        # Format recommendations with user details
        detailed_recommendations = []
        for rec_user_id, similarity_score in top_recommendations.items():
            user_details = self.users[self.users['user_id'] == rec_user_id].iloc[0]
            detailed_recommendations.append({
                'user_id': rec_user_id,
                'username': user_details['username'],
                'similarity_score': round(similarity_score * 100, 2),
                'favorite_genres': user_details['favorite_genres']
            })
        
        return detailed_recommendations

    def add_friend(self, user_id_1, user_id_2):
        """Add a new friend connection"""
        if user_id_1 == user_id_2:
            return "Cannot add yourself as a friend"
            
        # Check if friendship already exists
        existing_friendship = self.friend_connections[
            ((self.friend_connections['user_id_1'] == user_id_1) & 
             (self.friend_connections['user_id_2'] == user_id_2)) |
            ((self.friend_connections['user_id_1'] == user_id_2) & 
             (self.friend_connections['user_id_2'] == user_id_1))
        ]
        
        if not existing_friendship.empty:
            return "Friendship already exists"
            
        new_connection = {
            'user_id_1': min(user_id_1, user_id_2),  # Store IDs in consistent order
            'user_id_2': max(user_id_1, user_id_2),
            'connection_date': datetime.now().strftime('%Y-%m-%d')
        }
        self.friend_connections = pd.concat([self.friend_connections, pd.DataFrame([new_connection])], 
                                          ignore_index=True)
        return "Friendship added successfully"

    def get_user_stats(self, user_id):
        """Get gaming statistics for a user"""
        user_history = self.gaming_history[self.gaming_history['user_id'] == user_id]
        total_playtime = user_history['hours_played'].sum()
        games_played = len(user_history)
        friend_count = len(self.friend_connections[
            (self.friend_connections['user_id_1'] == user_id) |
            (self.friend_connections['user_id_2'] == user_id)
        ])
        
        return {
            'total_playtime': total_playtime,
            'games_played': games_played,
            'friend_count': friend_count
        }

if __name__ == "__main__":
    # Initialize platform
    platform = GamingSocialPlatform()
    
    # Demo usage
    print("Creating new user...")
    new_user = platform.create_user_profile(
        user_id=101,
        username="GameMaster",
        favorite_genres=["RPG", "Strategy"],
        playtime_hours=0
    )
    print(f"New user created: {new_user}")
    
    print("\nUpdating gaming history...")
    platform.update_gaming_history(101, 1, 5.5)
    platform.update_gaming_history(101, 2, 3.0)
    
    print("\nGetting friend recommendations...")
    recommendations = platform.get_friend_recommendations(101)
    print(json.dumps(recommendations, indent=2))
    
    print("\nGetting user stats...")
    stats = platform.get_user_stats(101)
    print(json.dumps(stats, indent=2))
