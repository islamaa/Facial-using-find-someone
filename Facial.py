import face_recognition
import requests
from bs4 import BeautifulSoup
import re

def encode_face(image_path):
    # Load the image file and encode the face
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        return face_encodings[0]
    else:
        raise ValueError("No faces found in the image.")

def search_social_media(image_encoding):
    # This function is a placeholder for actual search implementation
    # Currently, it just prints a message
    print("Searching social media for similar images...")

    # Example: Scraping a hypothetical site for images (replace with actual logic)
    url = "https://example-social-media-site.com/search"
    params = {'q': 'profile pictures'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_urls = [img['src'] for img in soup.find_all('img', src=True)]
        return image_urls
    else:
        return []

def compare_faces(image_encoding, image_urls):
    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            image = face_recognition.load_image_file(response.content)
            other_encodings = face_recognition.face_encodings(image)
            for other_encoding in other_encodings:
                results = face_recognition.compare_faces([image_encoding], other_encoding)
                if True in results:
                    print(f"Found a matching face at: {url}")
                    return url
    return None

if __name__ == "__main__":
    image_path = 'path_to_image.jpg'  # Replace with your image path
    try:
        face_encoding = encode_face(image_path)
        image_urls = search_social_media(face_encoding)
        if image_urls:
            match_url = compare_faces(face_encoding, image_urls)
            if match_url:
                print(f"Match found: {match_url}")
            else:
                print("No matching faces found.")
        else:
            print("No images found on social media.")
    except Exception as e:
        print(f"An error occurred: {e}")
