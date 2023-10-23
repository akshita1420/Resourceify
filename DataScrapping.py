import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://example.com'  # Replace with your target URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all unique links on the page
    unique_links = set()  # Using a set to store unique links
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http') or href.startswith('https'):
            unique_links.add(href)
    
    # Print the unique links
    for link in unique_links:
        print(link)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
