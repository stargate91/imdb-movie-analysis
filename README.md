# IMDb Movie Analysis

This is a beginner-friendly Python project where I explore and analyze movie data from the IMDb dataset. The goal was to practice loading, cleaning, analyzing, and visualizing real-world data, all using Python!

## What It Does

- Downloads IMDb datasets (automatically!)
- Loads and merges data from multiple .tsv files
- Analyzes:
  - Top 10 highest-rated movies
  - Average ratings by decade
  - Top directors (with at least 3 movies)
- Generates bar charts and line plots for each of the above
- Saves results as CSV and PNG files in the output folder

## Project Structure

```
imdb-movie-analysis/
├── data/                # IMDb .tsv files go here (downloaded automatically)
├── output/              # Results (CSV + charts) saved here
├── downloader.py        # Downloads and extracts the IMDb data
├── main.py              # Main script that runs the full pipeline
├── data_loader.py       # Loads and merges datasets
├── analysis.py          # Functions for calculating top movies, decades, etc.
├── visualize.py         # Generates plots from the analysis
├── requirements.txt     # Required packages (pandas, matplotlib)
├── .gitignore           # Ignores data and output in Git
└── README.md            # This file
```

## How to Run It

1. Make sure you have Python 3 installed
2. Install required packages (you can use a virtual environment if you like):

```bash
pip install -r requirements.txt
```

3. Download the data and run the analysis:

```bash
python downloader.py
python main.py
```

4. Check the output/ folder for results!

## Outputs

- output/top_10_movies.csv and top10_movies.png
- output/ratings_by_decade.csv and decade_ratings.png
- output/top_directors.csv and top_directors.png

## What I Learned

- How to use pandas for real dataset merging and cleaning
- Simple data analysis and grouping with groupby
- Creating plots with matplotlib
- Organizing code into multiple Python files (modularity)
- Using os, urllib, gzip, and file paths

## Author

Made by a junior Python developer learning how to analyze data with code. I built this to learn more about working with real datasets and writing modular Python scripts.

Feel free to fork or improve it!