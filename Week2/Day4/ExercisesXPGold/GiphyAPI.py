import requests

# Exercise 2

response = requests.get(
    'https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')

print(response)

if response.status_code == 200:
    gifs_data = response.json()

    filtered_gifs = [gif for gif in gifs_data['data'] if int(gif['images']['original']['height']) > 100]

    print(f"Number of GIFs with height > 100: {len(filtered_gifs)}")

    first_10_gifs = filtered_gifs[:10]

    for i, gif in enumerate(first_10_gifs, start=1):
        print(f"GIF {i}: {gif['url']}")
else:
    print("Failed to fetch GIFs. Status code:", response.status_code)


# Exercise 3
def fetch_gifs(search_term):
    api_key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
    endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}"

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        gifs = data.get('data', [])
        if gifs:
            return gifs
        else:
            return fetch_trending_gifs()
    else:
        return fetch_trending_gifs()

def fetch_trending_gifs():
    api_key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
    endpoint = f"https://api.giphy.com/v1/gifs/trending?api_key={api_key}"

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        gifs = data.get('data', [])
        return gifs
    else:
        return []

def main():
    search_term = input("Enter a term or phrase to search for GIFs: ")
    gifs = fetch_gifs(search_term)
    if gifs:
        print("Here are the relevant GIFs:")
        for gif in gifs:
            print(gif['url'])
    else:
        print("Sorry, we couldn't find any relevant GIFs. Here are the trending GIFs of the day:")
        trending_gifs = fetch_trending_gifs()
        for gif in trending_gifs:
            print(gif['url'])


main()
