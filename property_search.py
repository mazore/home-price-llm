import requests
from time import time
import traceback

def scrape_property_ids_from_search(location, number_properties, logger):
    """Takes in a location and the number of properties to scrape, and returns a list of property IDs
    by using the realtor.com API for searching properties.
    """
    url = 'https://www.realtor.com/api/v1/rdc_search_srp?client_id=rdc-search-for-sale-search&schema=vesta'
    headers = {'content-type': 'application/json'}
    with open('map_search_query.txt', 'r') as f:
        query = f.read()
    data = {
        'query': query,
        'variables': {
            'query': {'search_location': {'location': location}, 'status': ['for_sale', 'ready_to_build']},
            'limit': number_properties,
            'sort_type': 'relevant',
            'search_promotion': {'names': [], 'slots': []},
        },
    }
    t = time()
    resp = requests.post(url, headers=headers, json=data)
    try:
        search = resp.json()['data']['home_search']
    except Exception as e:
        traceback.print_exc()
        quit()
    logger.info(f'{search["count"]} properties found in {round(time() - t, 3)} seconds')
    return [property['property_id'] for property in search['properties']]
