import requests
from bs4 import BeautifulSoup

url = "https://discussions.unity.com/tag/openxr"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


posts = soup.find_all('span', class_='link-top-line')
for post in posts:
    title = post.find('a', class_='title').text.strip()
    print(title)