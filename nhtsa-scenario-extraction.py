from fars_cleaner import load_pipeline, FARSFetcher
#import fars_cleaner.datasets as ds
#from pooch import HTTPDownloader, create
#import requests
from pathlib import Path

import requests
from requests.exceptions import ConnectionError, Timeout
import time

def fetch_nhtsa_scenarios():
    PATH_FILE = Path("scenarios")
    cache_path = "fars-crashes"
    print("Fetching NHTSA scenarios*******************")
    fetcher = FARSFetcher(project_dir=PATH_FILE, cache_path=cache_path, show_progress=True)
    print("Fetching NHTSA scenarios...")

    retries = 3
    for attempt in range(retries):
        try:
            df = fetcher.fetch_single(2018)
            print("NHTSA scenarios fetched successfully.")
            return df
        except (ConnectionError, Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                raise

# Example usage
if __name__ == "__main__":
    try:
        nhtsa_scenarios = fetch_nhtsa_scenarios()
        print(nhtsa_scenarios.head())
    except Exception as e:
        print(f"Failed to fetch NHTSA scenarios: {e}")
"""
# 1. Créer une session requests avec un timeout plus long (par ex. 120 s)
session = requests.Session()
session.timeout = 120

# 2. Créer un downloader pooch qui utilisera cette session
downloader = HTTPDownloader(session=session)

# 3. Instancier votre récupérateur FARS en le forçant à utiliser le downloader custom
fetcher = ds.FARSFetcher(
    base_url="https://static.nhtsa.gov/nhtsa/downloads/FARS/",
    # selon la version de fars_cleaner, le paramètre peut s’appeler downloader ou http_downloader
    downloader=downloader
)

# 4. Tenter à nouveau de récupérer l’année souhaitée
try:
    df2018 = fetcher.fetch_single(2018)
    print("Chargement 2018 OK, nombre de lignes :", len(df2018))
except Exception as e:
    print("Ça a encore planté :", type(e).__name__, e)

"""