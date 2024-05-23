import re
from bs4 import BeautifulSoup

# Read the content of the policy.txt file
with open('exportPolicy.html', 'r') as f:
    content = f.read()

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Open a new file to write the output
with open('policy_extracted.txt', 'w') as out_file:
    # Iterate over each table row
    for tr in soup.find_all('tr'):
        # Find all table data cells within the row
        tds = tr.find_all('td')
        # Check if the row has at least two cells
        if len(tds) >= 2:
            # Get the text content of the first two cells
            policy = tds[0].get_text(strip=True)
            value = tds[1].get_text(strip=True) 
            value = re.sub(r"BUILTIN\\","",value)
            out_file.write(f"{policy}: {value}\n")


