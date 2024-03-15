import requests
import time


def get_webpage_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time


websites = ["https://familynekretnine.rs/",
            "https://www.google.com",
            "https://www.ynet.co.il",
            "https://www.imdb.com",
            "https://developers.institute/"]

for site in websites:
    load_time = get_webpage_load_time(site)
    print(f"Time taken to load {site}: {load_time:.2f} seconds")
