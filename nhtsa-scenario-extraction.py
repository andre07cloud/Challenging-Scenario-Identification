
from fars_cleaner import load_pipeline, FARSFetcher
import fars_cleaner.datasets as ds
from pooch import HTTPDownloader, create
import requests
from pathlib import Path

"""
def fetch_nhtsa_scenarios():


    PATH_FILE = Path("/home/andredejesus/Phd-Projects/Poly/Challenging-Scenario-Identification")
    cache_path = "fars-crashes"
    fetcher = FARSFetcher(project_dir=PATH_FILE, cache_path=cache_path, show_progress=True)
    #vehicles, acidents, people = load_pipeline(fetcher = fetcher, first_run=True, target_folder=PATH_FILE)
    print("Fetching NHTSA scenarios...")
    df = fetcher.fetch_single(2018)
    print("NHTSA scenarios fetched successfully.")


    return df

if __name__ == "__main__":
    crashes = fetch_nhtsa_scenarios()
    #print(df.shape)
    #print(df.head())
    #df.to_csv('nhtsa_scenarios.csv', index=False)
    print(crashes)
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

