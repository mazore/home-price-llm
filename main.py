import csv
import requests
from time import time

def scrape_property_data(property_id):
    """Takes in a property ID and returns a dictionary with the price, address, photo URL, and
    description of the house based on the realtor.com API. This can easily be adjusted to include
    square footage, number of bedrooms, etc.
    """
    headers = {  # Some required headers
        'content-type': 'application/json',
        'rdc-client-name': 'RDC_WEB_DETAILS_PAGE',
        'rdc-client-version': '2.1.6',
    }
    params = {
        'variables': '{"propertyId":"' + property_id + '"}',
        'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"17279788159d9fa5b7ad6c57c7f057714e73d30628a00929c1748d710865f52b"}}'
    }
    resp = requests.get('https://www.realtor.com/frontdoor/graphql?operationName=FullPropertyDetails', headers=headers, params=params)
    try:
        data = resp.json()
        home_info = data['data']['home']
    except Exception:
        raise Exception('Unknown error in search ' + resp.text)

    # Extract price
    list_price = home_info['list_price']

    # Extract address
    location = home_info['location']['address']
    address = f"{location['line']}, {location['city']} {location['state_code']} {location['postal_code']}"  # Address like "123 Main St, Bethlehem PA 18018"

    # Extract photo URL
    low_quality_photo_url = home_info['primary_photo']['href']
    high_quality_photo_url = low_quality_photo_url.replace('s.jpg', 'rd-w960_h720.webp')

    # Extract description
    description = home_info['description']['text']

    return {
        'price': list_price,
        'address': address,
        'photo_url': high_quality_photo_url,
        'description': description,
    }


def scrape_property_ids_from_search(location, number_properties):
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
            'query': {'search_location': {'location': location}},
            'limit': number_properties,
            'sort_type': 'relevant',
            'search_promotion': {'names': [], 'slots': []},
        },
    }
    t = time()
    resp = requests.post(url, headers=headers, json=data)
    try:
        search = resp.json()['data']['home_search']
    except Exception:
        raise Exception('Unknown error in search ' + resp.text)
    print(search['count'], 'properties found in', round(time() - t, 3), 'seconds')
    return [property['property_id'] for property in search['properties']]


if __name__ == '__main__':
    # Get user input
    location = input('What location do you want to search in (blank for Bethlehem): ') or 'Bethlehem, PA'
    number_properties = input('How many properties do you want to scrape (from 10-200): ') or '10'
    if not number_properties.isdigit() or not 10 <= int(number_properties) <= 200:
        raise ValueError('Number of properties must be an integer between 10 and 200')
    number_properties = int(number_properties)

    # Get search results for location
    property_ids = scrape_property_ids_from_search(location, number_properties)
    if len(property_ids) == 0:
        raise ValueError('No properties found for location: ' + location)

    # Get property data for each property
    all_property_data = []
    for i, property_id in enumerate(property_ids):
        t = time()
        property_data = scrape_property_data(property_id)
        print(f'Property {i + 1} of {len(property_ids)} scraped in', round(time() - t, 3), 'seconds')
        all_property_data.append(property_data)

    # Write to CSV
    with open('property_data.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_property_data[0].keys())
        writer.writeheader()
        writer.writerows(all_property_data)
