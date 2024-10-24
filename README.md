# Gaming Platform Social Feature

A Python-based social feature implementation for a gaming platform, focusing on friend recommendations based on gaming preferences and behavior. This project demonstrates the development of a social networking component that could be integrated into a larger gaming platform.

## Features

- User profile management
- Gaming history tracking
- Friend recommendations based on gaming similarity
- Friend connection system
- User statistics tracking

## Technical Implementation

The system uses several key technologies and approaches:

- **Pandas** for data management and analysis
- **Scikit-learn** for calculating user similarity
- **Cosine Similarity** for matching similar players
- **JSON** for data formatting and output

## Project Structure

```
gaming-platform-social/
│
├── data/
│   ├── users.csv
│   ├── gaming_history.csv
│   └── friend_connections.csv
│
├── main.py
├── generate_sample_data.py
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gaming-platform-social.git
cd gaming-platform-social
```

2. Install required packages:
```bash
pip install pandas numpy scikit-learn
```

3. Generate sample data:
```bash
python generate_sample_data.py
```

4. Run the main application:
```bash
python main.py
```

## Usage Example

```python
from main import GamingSocialPlatform

# Initialize the platform
platform = GamingSocialPlatform()

# Create a new user
new_user = platform.create_user_profile(
    user_id=101,
    username="GameMaster",
    favorite_genres=["RPG", "Strategy"]
)

# Update gaming history
platform.update_gaming_history(101, 1, 5.5)  # User 101 played game 1 for 5.5 hours

# Get friend recommendations
recommendations = platform.get_friend_recommendations(101)

# Get user stats
stats = platform.get_user_stats(101)
```

## Testing

Each function includes error handling and validation to ensure robust operation. The sample data generator creates realistic test data for development and testing purposes.

## Data Structure

### users.csv
- user_id: Unique identifier for each user
- username: User's display name
- favorite_genres: List of preferred game genres
- playtime_hours: Total hours played
- join_date: Date user joined the platform

### gaming_history.csv
- user_id: User identifier
- game_id: Game identifier
- hours_played: Time spent on the game
- last_played: Last play session date

### friend_connections.csv
- user_id_1: First user in connection
- user_id_2: Second user in connection
- connection_date: When the friendship was established

## Future Enhancements

1. Implement real-time chat functionality
2. Add group/clan features
3. Enhance recommendation algorithm with machine learning
4. Add achievement system
5. Implement event system for multiplayer sessions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
