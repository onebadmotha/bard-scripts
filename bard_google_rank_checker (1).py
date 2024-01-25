import requests
import bs4

def check_ranking(url):
  """Checks to see if a URL is ranked in Google Search and Google Images.

  Args:
    url: The URL to check.

  Returns:
    A tuple containing two booleans:
      - is_ranked_in_search: Whether the URL is ranked in Google Search.
      - is_ranked_in_images: Whether the URL is ranked in Google Images.
  """

  # Check Google Search.
  response = requests.get(f"https://www.google.com/search?q={url}")
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  # Get the top 10 search results.
  top_results = soup.select(".r .g")

  # Check if the URL is in the top 10 search results.
  is_ranked_in_search = False
  for result in top_results:
    if result.select_one("a")["href"] == url:
      is_ranked_in_search = True
      break

  # Check Google Images.
  response = requests.get(f"https://www.google.com/search?tbm=isch&q={url}")
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  # Get the top 10 image results.
  top_results = soup.select(".rg_i")

  # Check if the URL is in the top 10 image results.
  is_ranked_in_images = False
  for result in top_results:
    if result["data-src"] == url:
      is_ranked_in_images = True
      break

  return is_ranked_in_search, is_ranked_in_images

def main():
  """Prompts the user for a URL or image, and then checks to see if it is ranked in Google Search and Google Images."""

  # Get the URL or image from the user.
  url = input("Enter a URL or image: ")

  # Check the ranking.
  is_ranked_in_search, is_ranked_in_images = check_ranking(url)

  # Print the results.
  print(f"Is ranked in Google Search: {is_ranked_in_search}")
  print(f"Is ranked in Google Images: {is_ranked_in_images}")

if __name__ == "__main__":
  main()
import requests
import bs4

def check_ranking(url):
  """Checks to see if a URL is ranked in Google Search and Google Images.

  Args:
    url: The URL to check.

  Returns:
    A tuple containing two booleans:
      - is_ranked_in_search: Whether the URL is ranked in Google Search.
      - is_ranked_in_images: Whether the URL is ranked in Google Images.
  """

  # Check Google Search.
  response = requests.get(f"https://www.google.com/search?q={url}")
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  # Get the top 10 search results.
  top_results = soup.select(".r .g")

  # Check if the URL is in the top 10 search results.
  is_ranked_in_search = False
  for result in top_results:
    if result.select_one("a")["href"] == url:
      is_ranked_in_search = True
      break

  # Check Google Images.
  response = requests.get(f"https://www.google.com/search?tbm=isch&q={url}")
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  # Get the top 10 image results.
  top_results = soup.select(".rg_i")

  # Check if the URL is in the top 10 image results.
  is_ranked_in_images = False
  for result in top_results:
    if result["data-src"] == url:
      is_ranked_in_images = True
      break

  return is_ranked_in_search, is_ranked_in_images

def main():
  """Prompts the user for a URL or image, and then checks to see if it is ranked in Google Search and Google Images."""

  # Get the URL or image from the user.
  url = input("Enter a URL or image: ")

  # Check the ranking.
  is_ranked_in_search, is_ranked_in_images = check_ranking(url)

  # Print the results.
  print(f"Is ranked in Google Search: {is_ranked_in_search}")
  print(f"Is ranked in Google Images: {is_ranked_in_images}")

if __name__ == "__main__":
  main()
