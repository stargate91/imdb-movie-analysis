from data_loader import load_datasets
from analysis import (get_top_movies, get_best_decade, get_top_directors)
from visualize import (plot_top_movies, plot_decade_ratings, plot_top_directors)
import os

def main():
    df_merged, df_name = load_datasets()

    df_top10 = get_top_movies(df_merged)
    decade_avg = get_best_decade(df_merged)
    top_directors = get_top_directors(df_merged, df_name)

    os.makedirs("output", exist_ok=True)
    df_top10.to_csv("output/top_10_movies.csv", index=False)
    decade_avg.to_csv("output/ratings_by_decade.csv")
    top_directors.to_csv("output/top_directors.csv")

    plot_top_movies(df_top10)
    plot_decade_ratings(decade_avg)
    plot_top_directors(top_directors)

if __name__ == "__main__":
    main()