🎬 Movie Recommendation System
📌 Introduction
The Movie Recommendation System is a web-based application that provides personalized movie suggestions based on user preferences. It includes user authentication, history tracking, sequel suggestions, and a feedback mechanism to improve recommendations dynamically.

This system ensures better user engagement by allowing users to rate recommendations and refine their movie preferences.

🚀 Features
🎭 Movie Recommendation Engine
Users can enter their favorite movie, and the system suggests similar movies based on genres and previous ratings.
🔄 Sequel Suggestions
If a movie has sequels or spin-offs, they are suggested automatically.
⭐ User Rating and Feedback
Users rate recommendations on a 1-5 scale.
If the rating is low, the recommendations are adjusted dynamically.
Users can also remove specific movies from recommendations.
🔑 User Authentication
Users can sign up and log in to access personalized recommendations.
Login sessions are maintained until the user logs out.
📜 History Tracking
Stores previous searches and recommendations.
Users can view their search history anytime.
👤 User Profile Page
Displays username and user preferences.
Allows users to manage their recommendations.
🚪 Logout Functionality
Users can logout anytime, which clears their session data.
🛠️ Technologies Used
Technology	Purpose
Python	Core Programming Language
Streamlit	Web Framework for UI
SQLite	User and Feedback Database
Pandas	Data Handling and Processing
Random	Sampling and Movie Suggestions
Git & GitHub	Version Control and Deployment
🔧 Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/LikhitP12/movie-recommendation-system.git
cd movie-recommendation-system
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv .venv
3️⃣ Activate the Virtual Environment
sh
Copy
Edit
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
4️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
5️⃣ Run the Application
sh
Copy
Edit
streamlit run movie_recommendation.py
🎯 Usage Guide
1️⃣ Login / Sign Up
New users register using their username and password.
Existing users can log in to access their personalized movie suggestions.
2️⃣ Search for a Movie
Enter a movie name and click "Get Recommendations".
The system will display recommended movies and their details.
3️⃣ Rate the Recommendations
Users rate recommendations from 1 to 5.
4-5 → Keeps suggestions similar.
3 → Tweaks some recommendations.
1-2 → Changes recommendations completely.
4️⃣ Modify Preferences
Users can dislike certain movies to refine recommendations.
5️⃣ View Search History
Users can check previous searched movies and recommendations.
6️⃣ Logout
Clicking logout clears session data and ends the session.
📌 Future Enhancements
IMDb API Integration for real-time movie reviews and ratings.
Machine Learning-based Recommendations for more accuracy.
Movie Trailers and Summaries embedded in the UI.
Social Features to share recommendations with friends.
🏆 Developer Info
Developed by: Peethala V Siva Sampath Likhit & Pasumarthi Venkata Praveen
🎉 Contributing
🚀 Want to improve this project?

Fork the repository
Make changes
Submit a pull request
📜 License
This project is open-source under the MIT License.
