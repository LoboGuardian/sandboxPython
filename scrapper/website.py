import requests

def visit_website(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Successfully accessed the website!")
            print("HTML Content:")
            print(response.text)  # Print the full HTML content of the page
        else:
            print(f"Failed to access the website. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Replace 'https://example.com' with the URL you want to visit
url_to_visit = 'https://example.com'
visit_website(url_to_visit)
