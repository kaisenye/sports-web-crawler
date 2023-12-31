import requests
from bs4 import BeautifulSoup

print('hello world')
# URL of the page containing Steph Curry's stats
url = 'https://www.espn.com/nba/boxscore/_/gameId/401585067'

# Add a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Send a GET request with the added headers
response = requests.get(url, headers=headers)
print(response.status_code)

# Ensure the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract specific data
    # Update this according to the page structure
    stats = soup.find_all(attrs={'class': 'Table__TR Table__TR--sm Table__even'})

    # Process and print the stats
    for stat in stats:
        print(stat.text)
else:
    print(f"Error: Status code {response.status_code}")
