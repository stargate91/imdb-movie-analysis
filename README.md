# IMDb Movie Ratings Analyzer

Hi! This is a small Python project I created to practice working with real-world data using **Pandas** and **Matplotlib**. It analyzes movie ratings from the [IMDb Datasets](https://developer.imdb.com/non-commercial-datasets/) and gives some basic insights.

---

## What it does

This project answers 3 main questions:

1. **Top 10 movies** based on IMDb rating  
2. **Which decade** had the highest average movie rating?  
3. **Top directors** based on average rating (with at least 3 films)

It also generates:

- 3 CSV output files
- 3 charts (`.png`) using `matplotlib`

---

## Project Structure

movie_ratings_analyzer/
│
├── main.py # Main analysis script
├── setup_data.py # Download + extract IMDb datasets
├── /data # Folder for IMDb .tsv files (created automatically)
├── /output # CSV and chart outputs
└── README.md

---

## Setup

1. Make sure you have Python 3.10+ installed.
2. Install required packages:

```bash
pip install pandas matplotlib
```
Download the IMDb datasets using:
```bash
python setup_data.py
```

This will download and extract ~2.2 GB of TSV files into a data/ folder.

Run the analysis
```bash
python main.py
```
Outputs will be saved into the /output folder.

## Output Examples
output/top_10_movies.csv - Top rated movies
output/decade_ratings.png - Line chart of average rating by decade
output/top_directors.csv - Best directors with at least 3 movies

## What I learned
Reading large TSV files with pandas
Joining multiple datasets (merge(), groupby())
Dealing with missing values (na_values, dropna())
Creating charts with matplotlib
Writing modular and readable Python code

## To do next
Add user input options (e.g. top N movies)
Export to SQLite
Try seaborn visualizations
Add unit tests

Thanks for checking it out!