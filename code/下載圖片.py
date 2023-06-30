import requests

def download_images(image_links):
    for index, link in enumerate(image_links):
        try:
            response = requests.get(link)
            response.raise_for_status()
            with open(f"image_{index+1}.jpg", "wb") as file:
                file.write(response.content)
            print(f"Image {index+1} downloaded successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image {index+1}: {e}")

# Example usage
image_links = [
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300","https://picsum.photos/200/300","https://picsum.photos/200/300","https://picsum.photos/200/300",
]

download_images(image_links)