# Movie Recommendation System

## Introduction
The **Movie Recommendation System** is a web-based application that provides personalized movie suggestions based on user preferences. It includes user authentication, history tracking, sequel suggestions, and a feedback mechanism to improve recommendations dynamically.

## Features
- 🔑 **User Authentication**: Sign up, login, and session management.
- 🎬 **Movie Recommendations**: Suggests movies based on user input.
- 🔄 **Sequel Suggestions**: Displays sequels for selected movies.
- ⭐ **Feedback System**: Users can rate recommendations and refine future suggestions.
- 📜 **History Tracking**: Stores and displays past searches and recommendations.
- 👤 **Profile Page**: Displays user details and preferences.
- 🚪 **Logout Functionality**: Ends session and clears stored data.

## Technologies Used
- **Programming Language**: Python
- **Framework**: Streamlit
- **Database**: SQLite
- **Libraries**:
  - Pandas (Data Handling)
  - Random (Sampling)
  - SQLite3 (Database Management)

## Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/LikhitP12/movie-recommendation-system.git
cd movie-recommendation-system
```
### **2️⃣ Create a Virtual Environment**
```sh
python -m venv .venv
```
### **3️⃣ Activate the Virtual Environment**
```sh
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```
### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **5️⃣ Run the Application**
```sh
streamlit run movie_recommendation.py
```

## 🎯 Usage Guide
### **1️⃣ Login / Sign Up**
- New users **register** using their **username and password**.
- Existing users can **log in** to access their personalized movie suggestions.

### **2️⃣ Search for a Movie**
- Enter a movie name and click **"Get Recommendations"**.
- The system will display **recommended movies** and their details.

### **3️⃣ Rate the Recommendations**
- Users rate recommendations from **1 to 5**.
  - **4-5** → Keeps suggestions similar.
  - **3** → Tweaks some recommendations.
  - **1-2** → Changes recommendations completely.

### **4️⃣ Modify Preferences**
- Users can **dislike certain movies** to refine recommendations.

### **5️⃣ View Search History**
- Users can check previous **searched movies and recommendations**.

### **6️⃣ Logout**
- Clicking logout **clears session data** and ends the session.

## 📌 Future Enhancements
- **IMDb API Integration** for **real-time movie reviews and ratings**.
- **Machine Learning-based Recommendations** for more accuracy.
- **Movie Trailers and Summaries** embedded in the UI.
- **Social Features** to share recommendations with friends.

## 🏆 Developer Info
- **Developed by**: Peethala V Siva Sampath Likhit & Pasumarthi Venkata Praveen


## 🎉 Contributing
🚀 **Want to improve this project?**  
- Fork the repository  
- Make changes  
- Submit a pull request  

## 📜 License
This project is **open-source** under the **MIT License**.

---
