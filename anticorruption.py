import requests
from bs4 import BeautifulSoup
import json
# from explosive import log

# Step 1: Send a request to the web page
url = 'https://www.legisquebec.gouv.qc.ca/en/document/cs/L-6.1'  # Use your actual URL
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
finalObj = {}
label_groups = soup.select(".Heading.Heading .Label-group4")
header_divs = soup.select(".Heading.Heading")
obj = {}

def fetch_anticorruption_laws():
    if response.status_code == 200:
        # Step 3: Parse the HTML content
        # soup = BeautifulSoup(response.content, 'html.parser')
        # finalObj = {}

        # label_groups = soup.select(".Heading.Heading .Label-group4")
        # header_divs = soup.select(".Heading.Heading")
        # title_num = header_div.select_one(".Label-group4").get_text()
        # title_name = header_div.select_one(".TitleText-group4").get_text()
        # print(title_name)

        # for i,header_div in enumerate(header_divs):
        #     title_num = header_div.select_one(".Label-group4")
        #     title_name = header_div.select_one(".TitleText-group4")
        #     if(title_name and title_num):
        #         finalObj[title_num.get_text()] = title_name.get_text()
        # print(finalObj)

        # obj = {}
        chapters_array = ["#ga\:l_i","#ga\:l_ii","#ga\:l_iii","#ga\:l_iv","#ga\:l_v"]
        for chapter_id in chapters_array:
            fetchChapters(chapter_id)
        # print(obj)
        # print(json.dumps(obj))
        return {"ANTI-CORRUPTION ACT": obj}
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")

def fetchChapters(id):
    chapters = soup.select(id)
    for i,chapter in enumerate(chapters):
        descriptions = chapter.select(".section")
        title_num = chapter.select_one(".Label-group4")
        title_name = chapter.select_one(".TitleText-group4")
        section_array = []
        for section in descriptions:
            # print(section.select_one(".Subsection").get_text())
            single_section = section.select_one(".Subsection").get_text() 
            section_array.append(single_section)
            # print(single_section)
        if(title_num and title_name):
            obj[title_num.get_text()] ={
                "title": title_name.get_text(),
            }
            obj[title_num.get_text()]["sections"] = section_array
        # print("SECTONNNNNNNNN\n",section_array)

# Step 2: Check if the request was successful