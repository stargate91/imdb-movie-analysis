import os
import urllib.request
import gzip
import shutil

print("IMDb Dataset Downloader")
print("--------------------------")
print("Total required space after downloading and extracting the datasets: ~2.2 GB")
print("Target folder: \\data")
print()

urls = {
    "title.basics.tsv.gz": "https://datasets.imdbws.com/title.basics.tsv.gz",
    "title.crew.tsv.gz": "https://datasets.imdbws.com/title.crew.tsv.gz",
    "title.ratings.tsv.gz": "https://datasets.imdbws.com/title.ratings.tsv.gz",
    "name.basics.tsv.gz": "https://datasets.imdbws.com/name.basics.tsv.gz",
}

data_dir = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(data_dir, exist_ok=True)

for filename, url in urls.items():
    gz_path = os.path.join(data_dir, filename)
    tsv_path = gz_path[:-3]

    if not os.path.exists(tsv_path):
        print(f"Downloading: {filename}")
        urllib.request.urlretrieve(url, gz_path)

        print(f"Extracting: {filename}")
        with gzip.open(gz_path, 'rb') as f_in:
            with open(tsv_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"Cleaning up: {filename}")
        os.remove(gz_path)
    else:
        print(f"Already exists: {tsv_path}")

print(" \n All files downloaded and extracted successfully.")
print(" Compressed .gz files have been deleted.")
print(" You can now use the files in the '\\data' folder.")
print(" Done.")