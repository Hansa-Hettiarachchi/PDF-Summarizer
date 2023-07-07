import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_pdf_urls(target_h3_text):

    url = 'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=100'
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific h3 tag
        target_h3 = soup.find('h3', text=target_h3_text)

        # Find the next sibling dl tag after the target h3 tag
        dl_tag = target_h3.find_next_sibling('dl')

        # Find all dt tags within the dl tag
        dt_tags = dl_tag.find_all('dt')

        # Array to store URLs
        urls = []

        # Iterate through each dt tag
        for dt in dt_tags:
            # Find all 'a' tags within the current dt tag
            a_tags = dt.find_all('a', href=True)

            # Iterate through each 'a' tag
            for a in a_tags:
                # Get the link URL
                link_url = urljoin(url, a['href'])

                # Check if the link URL contains 'pdf'
                if 'pdf' in link_url.lower():
                    # Append the URL to the array
                    urls.append(link_url)

        # Return the list of URLs
        return urls

    else:
        print(
            f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []


# Usage example:
pdf_urls = get_pdf_urls('Fri, 7 Jul 2023')

# Print the URLs
print(pdf_urls)
print(len(pdf_urls))
