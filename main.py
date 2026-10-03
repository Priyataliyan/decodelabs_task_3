print("========================================")
print("     AI RECOMMENDATION SYSTEM         ")
print("========================================")


movies = [
    {
        "name": "Interstellar",
        "genres": ["sci-fi", "adventure", "drama"]
    },
    {
        "name": "Inception",
        "genres": ["sci-fi", "action", "thriller"]
    },
    {
        "name": "The Dark Knight",
        "genres": ["action", "crime", "thriller"]
    },
    {
        "name": "Titanic",
        "genres": ["romance", "drama"]
    },
    {
        "name": "The Hangover",
        "genres": ["comedy"]
    },
    {
        "name": "Avengers: Endgame",
        "genres": ["action", "adventure", "sci-fi"]
    },
    {
        "name": "The Notebook",
        "genres": ["romance", "drama"]
    }
]



user_input = input(
    "\nEnter your interests separated by comma: "
)

user_preferences = []

for item in user_input.split(","):
    preference = item.strip().lower()

    if preference != "":
        user_preferences.append(preference)

recommendations = []

for movie in movies:
    score = 0

    for genre in movie["genres"]:
        if genre in user_preferences:
            score = score + 1

    if score > 0:
        recommendations.append((movie["name"], score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\n----------------------------------------")
print("        RECOMMENDED MOVIES")
print("----------------------------------------")

if len(recommendations) == 0:
    print("Sorry, no matching movies found.")
    print("Try interests like:")
    print("Action, Comedy, Sci-Fi, Romance, Thriller")

else:
    for name, score in recommendations:
        print(name, "- Similarity Score:", score)


print("\nThank you for using the AI Recommendation System!")