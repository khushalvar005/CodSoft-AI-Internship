import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie dataset
movies = {
    "title": [
        "The Avengers",
        "Iron Man",
        "Thor",
        "The Dark Knight",
        "Batman Begins",
        "Interstellar",
        "Inception",
        "Titanic",
        "The Notebook",
        "Avatar",
        "Spider-Man",
        "Doctor Strange"
    ],
    "genre": [
        "action superhero adventure",
        "action superhero science fiction",
        "action fantasy adventure",
        "action crime thriller superhero",
        "action crime superhero",
        "science fiction space drama",
        "science fiction thriller action",
        "romance drama tragedy",
        "romance drama",
        "science fiction adventure fantasy",
        "action superhero adventure",
        "action fantasy magic"
    ]
}

df = pd.DataFrame(movies)

# Convert movie genres into numerical features using TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["genre"])

# Calculate similarity between movies
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend_movies(movie_name, num_recommendations=5):
    # Find the movie in the dataset
    matches = df[df["title"].str.lower() == movie_name.lower()]

    if matches.empty:
        print("Movie not found in the dataset.")
        print("Available movies:", ", ".join(df["title"]))
        return

    movie_index = matches.index[0]

    # Calculate similarity scores
    scores = list(enumerate(similarity[movie_index]))

    # Sort movies by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nMovies similar to '{df.iloc[movie_index]['title']}':\n")

    count = 0

    for index, score in scores:
        if index != movie_index:
            print(f"{df.iloc[index]['title']} (Similarity: {score:.2f})")
            count += 1

        if count == num_recommendations:
            break


# Main program
print("=" * 40)
print("       MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

print("\nAvailable Movies:")
for movie in df["title"]:
    print("-", movie)

while True:
    movie_name = input(
        "\nEnter a movie you like (or type 'exit' to quit): "
    ).strip()

    if movie_name.lower() == "exit":
        print("Thank you for using the recommendation system!")
        break

    try:
        num = int(input("How many recommendations do you want? "))

        if num < 1:
            print("Please enter a number greater than zero.")
            continue

        recommend_movies(movie_name, num)

    except ValueError:
        print("Please enter a valid number.")