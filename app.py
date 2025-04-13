from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
df = pd.read_csv("movies.csv")
vectorizer = TfidfVectorizer()
genre_vectors = vectorizer.fit_transform(df['genre'])
similarity_matrix = cosine_similarity(genre_vectors)

def get_recommendations(title, top_n=3):
    try:
        idx = df[df['title'].str.lower() == title.lower()].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        return [df.iloc[i[0]]['title'] for i in sim_scores]
    except:
        return ["Sorry, that title isn't in our system."]

@app.route("/api/messages", methods=["POST"])
def messages():
    data = request.get_json()
    user_input = data.get("text", "")
    print("User input:", user_input)

    recommendations = get_recommendations(user_input)
    bot_reply = f"Recommended for you: {', '.join(recommendations)}"
    print("Bot reply:", bot_reply)

    # Respond with full activity structure for Bot Framework
    return jsonify({
        "type": "message",
        "text": bot_reply,
        "from": {
            "id": "bot",
            "name": "MovieRecommenderBot"
        },
        "recipient": {
            "id": data.get("from", {}).get("id", "user"),
            "name": data.get("from", {}).get("name", "User")
        },
        "replyToId": data.get("id", "")
    })


if __name__ == "__main__":
    app.run(port=3978)
