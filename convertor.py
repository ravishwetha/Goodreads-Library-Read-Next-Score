import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML content from the text file
with open('book_list.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table', {'id': 'books'})

# Extract the headers
headers = ['title', 'num_pages', 'avg_rating', 'num_ratings', 'shelves', 'actions']

# Extract the rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    row = []
    
    # Extract title
    title = tr.find('td', {'class': 'field title'}).find('a').text.strip()

    # Extract author
    author = tr.find('td', {'class': 'field author'}).find('a').text.strip()
    
    # Extract num_pages
    num_pages_td = tr.find('td', {'class': 'field num_pages'})
    num_pages = num_pages_td.get_text(strip=True).replace('pp', '').replace('num pages', '').strip() if num_pages_td else 'unknown'
    
    # Extract my rating
    my_rating_td = tr.find('td', {'class': 'field rating'})
    my_rating = my_rating_td.get_text(strip=True).replace('rating', '').strip() if my_rating_td else 'unknown'

    # Extract avg_rating
    avg_rating_td = tr.find('td', {'class': 'field avg_rating'})
    avg_rating = avg_rating_td.get_text(strip=True).replace('avg rating', '').strip() if avg_rating_td else 'unknown'
    
    # Extract num_ratings
    num_ratings_td = tr.find('td', {'class': 'field num_ratings'})
    num_ratings = num_ratings_td.get_text(strip=True).replace('num ratings', '').replace(',', '').strip() if num_ratings_td else 'unknown'

    # Extract shelf
    shelves_td = tr.find('td', {'class': 'field shelves'})
    shelves = shelves_td.get_text(strip=True).replace('shelves', '').replace(',', '').strip() if shelves_td else 'unknown'
    
    # Extract actions
    actions_td = tr.find('td', {'class': 'field actions'})
    actions = ' '.join([a.text.strip() for a in actions_td.find_all('a')]) if actions_td else ''
    
    row.extend([title, author, num_pages, my_rating, avg_rating, num_ratings, shelves, actions])
    rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv('book_list.csv', index=False)

print('CSV file has been created successfully.')
