import requests
import matplotlib.pyplot as plt

# ✅ Only your API key here (not full URL!)
API_KEY = "a94f5d76"   # replace with your own key
BASE_URL = "http://www.omdbapi.com/"

def get_movie_data(response):
    """Show movie details"""
    print(f"\n🎬 Movie: {response['Title']}")
    print(f"⭐ IMDB Rating: {response.get('imdbRating', 'N/A')}")

def get_series_data(title, response):
    """Fetch series details season by season and plot ratings"""
    total_seasons = int(response["totalSeasons"])
    print(f"\n📺 Web Series: {response['Title']}")
    print(f"Total Seasons: {total_seasons}\n")

    season_avg = {}  # store average rating per season

    for season in range(1, total_seasons + 1):
        season_params = {"t": title, "Season": season, "apikey": API_KEY}
        season_data = requests.get(BASE_URL, params=season_params).json()

        print(f"--- Season {season} ---")
        ratings = []
        episodes = []

        for ep in season_data.get("Episodes", []):
            ep_num = ep.get("Episode")
            ep_title = ep.get("Title")
            ep_rating = ep.get("imdbRating", "N/A")

            if ep_rating == "N/A":
                print(f"Episode {ep_num}: {ep_title} → Rating not updated yet")
            else:
                print(f"Episode {ep_num}: {ep_title} → {ep_rating}")
                ratings.append(float(ep_rating))
                episodes.append(int(ep_num))

        # Plot season ratings
        if ratings:
            plt.plot(episodes, ratings, marker="o", label=f"Season {season}")
            season_avg[f"Season {season}"] = round(sum(ratings) / len(ratings), 2)
        else:
            season_avg[f"Season {season}"] = "No ratings yet"

    # Print average ratings
    print("\n📊 Average Ratings per Season:")
    for s, avg in season_avg.items():
        print(f"{s}: {avg}")

    # Final Graph
    plt.title(f"IMDB Ratings of '{response['Title']}'")
    plt.xlabel("Episodes")
    plt.ylabel("IMDB Rating")
    plt.ylim(0, 10)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    query = input("Enter movie or web series name: ").strip()

    # Step 1: Try search for suggestions
    params = {"s": query, "apikey": API_KEY}
    search_response = requests.get(BASE_URL, params=params).json()

    if search_response.get("Response") == "True":
        results = search_response.get("Search", [])
        print("\n🔎 Did you mean:")
        for i, item in enumerate(results, 1):
            print(f"{i}. {item['Title']} ({item.get('Year', 'N/A')}) [{item.get('Type')}]")

        choice = input("\nEnter the number of the correct title: ")
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            title = results[int(choice) - 1]["Title"]
        else:
            print("❌ Invalid choice. Exiting.")
            return
    else:
        # Step 2: Fallback to exact title search
        print("⚠️ Suggestions unavailable, trying exact title match...")
        title = query

    # Fetch full details using exact title
    params = {"t": title, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params).json()

    if response.get("Response") == "True":
        if response["Type"] == "movie":
            get_movie_data(response)
        elif response["Type"] == "series":
            get_series_data(title, response)
    else:
        print("❌ Title not found. Please check spelling or try again later.")

if __name__ == "__main__":
    main()
