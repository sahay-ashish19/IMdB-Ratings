Here’s a clean **README.md** for your project:

---

# 🎬 Movie & Web Series IMDB Ratings Analyzer

This Python project fetches **movie** and **web series** details from the [OMDb API](https://www.omdbapi.com/) and displays ratings in a **clear tabular format** with a **visual graph of episode ratings** season by season.

It helps you quickly explore movies, web series, and analyze how their ratings change across episodes and seasons.

---

## 🚀 Features

* 🔎 **Search Suggestions**: Finds multiple matches for a given movie/series name.
* 🎥 **Movie Mode**: Shows IMDB rating of a movie.
* 📺 **Series Mode**: Fetches details season by season, printing each episode rating.
* 📊 **Graphical Insights**: Plots episode-wise ratings for each season using `matplotlib`.
* 📈 **Season Averages**: Displays the average IMDB rating per season.

---

## 📂 Project Structure

```
📦 Movie-Series-Ratings-Analyzer
 ┣ 📜 main.py         # Main script
 ┣ 📜 README.md       # Documentation (this file)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sahay-ashish19/IMdB-Ratings.git
cd IMdB-Ratings
```

### 2️⃣ Install dependencies

Make sure you have **Python 3.x** installed. Then run:

```bash
pip install requests matplotlib
```

### 3️⃣ Get OMDb API Key

* Visit [OMDb API](https://www.omdbapi.com/apikey.aspx)
* Generate a free API key (1000 requests/day)
* Replace the placeholder in `main.py`:

```python
API_KEY = "your_api_key_here"
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Example:

```
Enter movie or web series name: Mirzapur

🔎 Did you mean:
1. Mirzapur (2018–) [series]
2. Mirzapur Promo: Bonus Deleted Scenes (2024) [movie]
3. Mirzapur (2026) [movie]

Enter the number of the correct title: 1
```

📺 If it’s a series, you’ll get:

* Episode ratings
* Season average ratings
* A plotted graph of ratings

🎥 If it’s a movie, you’ll get:

* Title
* IMDB rating

---

## 📊 Sample Output (Graph)

For a series like **Mirzapur**, ratings per episode are plotted season by season:

```
📊 Average Ratings per Season:
Season 1: 8.34
Season 2: 7.2
Season 3: 6.5
```

*(Graph opens in a new window)*

### 📷 Screenshot
<img width="640" height="480" alt="Mirzapur" src="https://github.com/user-attachments/assets/b4147f9f-d089-4810-ae2f-8bcefddf9fc0" />



---

## 🛠️ Tech Stack

* **Python** (3.x)
* **Requests** (for API calls)
* **Matplotlib** (for plotting)
* **OMDb API** (movie/series data)

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to add features (e.g., Rotten Tomatoes ratings, export to CSV/Excel), feel free to fork and submit.

---
