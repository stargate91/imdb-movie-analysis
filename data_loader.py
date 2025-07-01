import os
import pandas as pd

def load_datasets():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")

    basics = pd.read_csv(os.path.join(data_dir, "title.basics.tsv"), sep="\t", na_values="\\N", dtype=str)
    crew = pd.read_csv(os.path.join(data_dir, "title.crew.tsv"), sep="\t", na_values="\\N", dtype=str)
    ratings = pd.read_csv(os.path.join(data_dir, "title.ratings.tsv"), sep="\t", na_values="\\N", dtype=str)
    names = pd.read_csv(os.path.join(data_dir, "name.basics.tsv"), sep="\t", na_values="\\N", dtype=str)

    basics = basics[basics["titleType"] == "movie"]

    df_merged = pd.merge(basics, ratings, on="tconst", how="inner")
    df_merged = pd.merge(df_merged, crew, on="tconst", how="inner")




    return df_merged, names