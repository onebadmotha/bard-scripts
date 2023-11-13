import requests

# Function to change the User-Agent to simulate Google Image Bot
def change_user_agent_to_google_image_bot(url):
    headers = {
        'User-Agent': 'Googlebot-Image/1.0'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Prompt the user for a URL
url = input("Enter the URL of the image: ")

# Attempt to request the image with Google Image Bot User-Agent
image_response = change_user_agent_to_google_image_bot(url)

if image_response:
    if image_response.status_code == 200:
        # Image successfully fetched
        with open('image.jpg', 'wb') as f:
            f.write(image_response.content)
        print("Image downloaded successfully as 'image.jpg'")
    else:
        print(f"Failed to fetch the image. Status code: {image_response.status_code}")
else:
    print("Image request failed with Google Image Bot User-Agent.")

