# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# # URL of the website to scrape
# url = 'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=100'

# # Send a GET request to the website
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find the specific h3 tag
#     target_h3 = soup.find('h3', text='Fri, 7 Jul 2023')

#     # Find the next sibling dl tag after the target h3 tag
#     dl_tag = target_h3.find_next_sibling('dl')

#     # Find all dt tags within the dl tag
#     dt_tags = dl_tag.find_all('dt')

#     # Iterate through each dt tag
#     for dt in dt_tags:
#         # Find all 'a' tags within the current dt tag
#         a_tags = dt.find_all('a', href=True)

#         # Iterate through each 'a' tag
#         for a in a_tags:
#             # Get the link URL
#             link_url = urljoin(url, a['href'])

# #             # Check if the link URL contains 'pdf'
# #             if 'pdf' in link_url.lower():
# #                 # Get the link text
# #                 link_text = a.get_text(strip=True)

# #                 # Print the link text and URL
# #                 print(f"Link Text: {link_text}")
# #                 print(f"URL: {link_url}")
# #                 print()
# # else:
#     print(
#         f"Failed to retrieve the webpage. Status code: {response.status_code}")


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website to scrape
url = 'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=100'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific h3 tag
    target_h3 = soup.find('h3', text='Fri, 7 Jul 2023')

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
                # Get the link text
                link_text = a.get_text(strip=True)

                # Append the URL to the array
                urls.append(link_url)

else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Print the URLs
print(urls)
