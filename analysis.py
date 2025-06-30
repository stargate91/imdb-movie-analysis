import pandas as pd

def get_top_movies(df):
    df = df[["primaryTitle", "averageRating", "startYear"]].dropna()
    df["averageRating"] = df["averageRating"].astype(float)
    return df.sort_values(by="averageRating", ascending=False).head(10)

def get_best_decade(df):
    df = df[["startYear", "averageRating"]].dropna()
    df["startYear"] = pd.to_numeric(df["startYear"], errors="coerce")
    df["averageRating"] = pd.to_numeric(df["averageRating"], errors="coerce")
    df = df.dropna()
    df["decade"] = (df["startYear"] // 10) * 10
    return df.groupby("decade")["averageRating"].mean()

def get_top_directors(df, df_names):
    df_directors = df[["tconst", "directors", "averageRating"]].copy()
    df_directors = df_directors.dropna(subset=["directors"])
    df_directors["averageRating"] = pd.to_numeric(df_directors["averageRating"], errors="coerce")
    df_directors["director_id"] = df_directors["directors"].str.split(",")
    df_directors = df_directors.explode("director_id")
    df_named = pd.merge(df_directors, df_names[["nconst", "primaryName"]], left_on="director_id", right_on="nconst", how="left")
    df_named = df_named.dropna(subset=["primaryName", "averageRating"])

    grouped = df_named.groupby("primaryName").agg(num_movies=("tconst", "count"),avg_rating=("averageRating", "mean"))
    return grouped[grouped["num_movies"] >= 3].sort_values("avg_rating", ascending=False)