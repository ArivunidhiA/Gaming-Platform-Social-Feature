import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_data():
    # Generate users data
    users_data = {
        'user_id': range(1, 21),
        'username': [f'Player{i}' for i in range(1, 21)],
        'favorite_genres': [
            ['RPG', 'Strategy'],
            ['FPS', 'Sports'],
            ['Adventure', 'RPG'],
            ['Strategy', 'Simulation'],
            ['Sports', 'Racing'],
            ['FPS', 'Battle Royale'],
            ['RPG', 'MMORPG'],
            ['Racing', 'Sports'],
            ['Strategy', 'Card Games'],
            ['Adventure', 'Platform'],
            ['FPS', 'RPG'],
            ['Sports', 'Simulation'],
            ['Strategy', 'Card Games'],
            ['RPG', 'Adventure'],
            ['Racing', 'Sports'],
            ['FPS', 'Strategy'],
            ['Adventure', 'Platform'],
            ['RPG', 'MMORPG'],
            ['Sports', 'Strategy'],
            ['FPS', 'Battle Royale']
        ],
        'playtime_hours': np.random.randint(10, 1000, 20),
        'join_date': [
            (datetime.now() - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d')
            for _ in range(20)
        ]
    }
    
    # Generate gaming history data
    gaming_history_data = []
    for user_id in range(1, 21):
        num_games = np.random.randint(3, 10)
        for _ in range(num_games):
            gaming_history_data.append({
                'user_id': user_id,
                'game_id': np.random.randint(1, 11),  # 10 different games
                'hours_played': np.random.randint(1, 100),
                'last_played': (datetime.now() - timedelta(days=np.random.randint(1, 30))).strftime('%Y-%m-%d')
            })
    
    # Generate friend connections data
    friend_connections_data = []
    for _ in range(30):  # Generate 30 random friendships
        user_id_1 = np.random.randint(1, 21)
        user_id_2 = np.random.randint(1, 21)
        if user_id_1 != user_id_2:  # Avoid self-friendships
            friend_connections_data.append({
                'user_id_1': min(user_id_1, user_id_2),  # Store IDs in consistent order
                'user_id_2': max(user_id_1, user_id_2),
                'connection_date': (datetime.now() - timedelta(days=np.random.randint(1, 180))).strftime('%Y-%m-%d')
            })
    
    # Create DataFrames
    users_df = pd.DataFrame(users_data)
    gaming_history_df = pd.DataFrame(gaming_history_data)
    friend_connections_df = pd.DataFrame(friend_connections_data).drop_duplicates(
        subset=['user_id_1', 'user_id_2']
    )
    
    # Save to CSV files
    users_df.to_csv('data/users.csv', index=False)
    gaming_history_df.to_csv('data/gaming_history.csv', index=False)
    friend_connections_df.to_csv('data/friend_connections.csv', index=False)

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
    
    generate_sample_data()
    print("Sample data generated successfully!")
