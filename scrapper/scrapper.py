import requests
from bs4 import BeautifulSoup

def visit_and_scrape_website(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Successfully accessed the website!")
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Print the title of the page
            title = soup.title.string
            print(f"Page Title: {title}")

            # Example: Find all paragraphs
            paragraphs = soup.find_all('p')
            for i, paragraph in enumerate(paragraphs):
              print(f"Paragraph {i+1}: {paragraph.get_text()}")
        else:
            print(f"Failed to access the website. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Replace 'https://example.com' with the URL you want to visit
url_to_visit = 'https://example.com'
visit_and_scrape_website(url_to_visit)
