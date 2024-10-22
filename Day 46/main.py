import bs4
import requests

theYear = input("Enter the year like this YYYY-MM-DD: ")
theURL = f"https://www.billboard.com/charts/hot-100/{theYear}"

# Add headers to mimic a browser request
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(theURL, headers=headers)

# Ensure the request was successful
if response.status_code == 200:
  soup = bs4.BeautifulSoup(response.text, "html.parser")

  # Find all li elements with the specific class for the chart results
  theDivs = soup.find_all("li", {"class": "o-chart-results-list__item"})

  # Loop through each div
  for div in theDivs:
    # Find the song title in the 'h3' tag
    song_title = div.find("h3", {"id": "title-of-a-story"})

    # Find the artist name by searching for any span with the class 'c-label'
    artist_name = div.find("span", {"class": "c-label"})

    # Print the song title and artist name if they are found
    if song_title:
      if artist_name:
        print(f"Song: {song_title.text.strip()} | Artist: {artist_name.text.strip()}")
      else:
        print(f"Song: {song_title.text.strip()} | Artist: Not found")
else:
  print(f"Failed to retrieve the page. Status code: {response.status_code}")
# Im gonna stop here because spotify verification is not working right now
