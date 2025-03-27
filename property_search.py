import requests
from time import time
import traceback

with open('map_search_query.txt', 'r') as f:
    query = f.read()

def scrape_property_ids_from_search(location, number_properties, logger=None):
    """Takes in a location and the number of properties to scrape, and returns a list of unique property IDs
    by using the realtor.com API for searching properties.
    """
    print_info = print
    if logger is not None:
        print_info = logger.info

    url = 'https://www.realtor.com/api/v1/rdc_search_srp?client_id=rdc-search-for-sale-search&schema=vesta'
    headers = {'content-type': 'application/json'}

    data = {
        'query': query,
        'variables': {
            'query': {
                'search_location': {'location': location},
                'status': ['for_sale', 'ready_to_build'],
            },
            'limit': None,  # To be set in the loop
            'offset': None,  # To be set in the loop
            'sort_type': 'relevant',
            'search_promotion': {'names': [], 'slots': []},
        },
    }

    t_total = time()
    property_ids = set()
    offset = 0

    while len(property_ids) < (number_properties - 10):
        limit = min(200, number_properties - len(property_ids))
        data['variables']['limit'] = limit
        data['variables']['offset'] = offset

        t = time()
        resp = requests.post(url, headers=headers, json=data)
        try:
            search = resp.json()['data']['home_search']
        except Exception as e:
            traceback.print_exc()
            break

        properties = search.get('properties', [])
        if not properties:
            break

        property_ids.update(property['property_id'] for property in properties)
        print_info(f"Retrieved {len(properties)} properties (Total collected: {len(property_ids)}) in {round(time() - t, 3)} seconds")

        if len(properties) < limit:
            # No more properties available
            break

        offset += limit

    print_info(f'Total {len(property_ids)} unique properties found in {round(time() - t_total, 3)} seconds')
    return list(property_ids)[:number_properties]


if __name__ == '__main__':
    ids = scrape_property_ids_from_search('Seattle, WA', 1000)
    print(ids)
    print(len(ids))
