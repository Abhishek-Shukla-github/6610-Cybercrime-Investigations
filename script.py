import requests
from bs4 import BeautifulSoup
import json
from anticorruption import fetch_anticorruption_laws
from explosive import fetch_explosive_laws
from tear_bombs import fetch_tear_bomb_laws
from syndical import fetch_syndical_laws
from firearm_protection import fetch_firearm_protection_laws

# Step 2: Check if the request was successful
    # Step 3: Parse the HTML content
# anticorruption_result = fetch_anticorruption_laws()
# explosive_laws_result = fetch_explosive_laws()
finalObj = [fetch_anticorruption_laws(), fetch_explosive_laws(), fetch_tear_bomb_laws(), fetch_syndical_laws(),fetch_firearm_protection_laws()]


print(json.dumps(finalObj))