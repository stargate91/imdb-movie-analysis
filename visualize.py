import matplotlib.pyplot as plt
import os

def plot_top_movies(df):
    plt.figure(figsize=(10, 6))
    plt.barh(df["primaryTitle"], df["averageRating"], color="skyblue")
    plt.xlabel("Average rating")
    plt.title("Top 10 movies by IMDb rating")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("output/top10_movies.png")
    plt.close()

def plot_decade_ratings(decade_avg):
    plt.figure(figsize=(10, 5))
    plt.plot(decade_avg.index.astype(int), decade_avg.values, marker="o", linestyle="-", color="darkgreen")
    plt.title("Average IMDb rating by decade")
    plt.xlabel("Decade")
    plt.ylabel("Average rating")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/decade_ratings.png")
    plt.close()

def plot_top_directors(df):
    top = df.head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top.index, top["avg_rating"], color="coral")
    plt.xlabel("Average rating")
    plt.title("Top 10 directors (at least 3 films)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("output/top_directors.png")
    plt.close()