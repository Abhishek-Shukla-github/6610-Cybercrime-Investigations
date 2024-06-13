import requests
from bs4 import BeautifulSoup
import json
# from explosive import log

# Step 1: Send a request to the web page
url = 'https://www.legisquebec.gouv.qc.ca/en/document/cs/P-38.0001'  # Use your actual URL
# url = 'https://www.legisquebec.gouv.qc.ca/en/document/cs/E-22'  # Use your actual URL
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
finalObj = {}
label_groups = soup.select(".Heading.Heading .Label-group4")
header_divs = soup.select(".Heading.Heading")
obj = {}

def fetch_firearm_protection_laws():
    if response.status_code == 200:
        return fetchChapters()
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    

def fetchChapters():
    chapters = soup.select(".LegislativeDocument.Global.Style_Extra_Class")
    for i,chapter in enumerate(chapters):
        descriptions = chapter.select(".section")
        title_num = "chapter P-38.0001"
        title_name = "ACT TO PROTECT PERSONS WITH REGARD TO ACTIVITIES INVOLVING FIREARMS"
        section_array = []
        for section in descriptions:
            single_section = section.select_one(".Subsection").get_text() 
            section_array.append(single_section)
            
        obj[title_num] ={
            "title": title_name,
        }
        obj[title_num]["sections"] = section_array
        # print(obj)
    return {"ACT TO PROTECT PERSONS WITH REGARD TO ACTIVITIES INVOLVING FIREARMS": obj}

# fetch_firearm_protection_laws()