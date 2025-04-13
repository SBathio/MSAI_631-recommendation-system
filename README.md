
# MSAI_631 Recommendation System Project

This project is part of the **AI for Human-Computer Interaction** course (MSAI 631) at the University of the Cumberlands. It demonstrates how to create a content-based recommendation system using artificial intelligence (AI) techniques integrated with human-computer interaction (HCI) principles. The application includes a conversational interface using the **Bot Framework Emulator** and is designed to simulate intelligent recommendations based on user input.

---

## 🚀 Project Overview

- **Model Type:** Content-Based Filtering
- **Domain:** Movie Recommendations
- **Interface:** Chatbot via Microsoft Bot Framework Emulator
- **Backend:** Python + Flask + Scikit-learn
- **Development Platform:** Google Colab and Local Flask Server

---

## 🧠 Features

- Conversational chatbot to recommend similar movies
- Natural language-based user input
- Cosine similarity-based recommendation logic
- Lightweight, interpretable design for educational use
- Integration-ready Flask API endpoint for any chatbot UI

---

## 📁 Project Structure

```
MSAI_631-recommendation-system/
│
├── app.py                     # Flask app for chatbot API
├── movies.csv                 # Sample movie dataset
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .env                       # Optional (for API keys, if needed)
```

---

## ⚙️ How to Run the Project Locally

1. **Clone this repository**

```bash
git clone https://github.com/SBathio/MSAI_631-recommendation-system.git
cd MSAI_631-recommendation-system
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask application**

```bash
python app.py
```

4. **Test with Bot Framework Emulator**
   - Open Emulator
   - Connect to: `http://localhost:3978/api/messages`
   - Type a movie title like `"Inception"` to get recommendations

---

## 🧪 Dataset Used

The system uses a simplified content-based approach based on a `movies.csv` dataset, which includes movie titles and associated genres.

---

## 🤖 Technologies Used

- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- Microsoft Bot Framework Emulator
- Google Colab (for initial prototype and data exploration)

---

## 🌟 Future Enhancements

- Integrate sentiment-based personalization
- Expand to hybrid recommendation system (content + collaborative)
- Add voice interface using Azure Speech SDK
- Store user preferences and session history

---

## 📚 References

- Ricci, F., Rokach, L., & Shapira, B. (2011). *Introduction to Recommender Systems Handbook*. Springer.
- Microsoft. (n.d.). *Bot Framework Emulator*. https://github.com/microsoft/BotFramework-Emulator
- Scikit-learn documentation: https://scikit-learn.org/

---

## 👨‍💻 Author

**Sigou Bathily**  
AI for HCI – MSAI 631  
University of the Cumberlands  
