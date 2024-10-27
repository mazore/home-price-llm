import csv
import json
import requests
from FullPropertyDetailsResponse import FullPropertyDetailsResponse
from LocationScoresResponse import LocationScoresResponse
from time import time

def graphql_request(operation_name, variables, sha_hash):
    url = f'https://www.realtor.com/frontdoor/graphql'
    headers = {  # Some required headers
        'content-type': 'application/json',
        'rdc-client-name': 'RDC_WEB_DETAILS_PAGE',
        'rdc-client-version': '2.1.6',
    }
    params = {
        'operationName': operation_name,
        'variables': json.dumps(variables),
        'extensions': json.dumps({"persistedQuery": {"version": 1, "sha256Hash": sha_hash}})
    }

    resp = requests.get(url, headers=headers, params=params)
    return resp.json()

def scrape_property_data(property_id):
    """Takes in a property ID and returns a dictionary with the price, address, photo URL, and
    description of the house based on the realtor.com API. This can easily be adjusted to include
    square footage, number of bedrooms, etc.
    """
    variables = {'propertyId': property_id}
    full_details_resp_json = graphql_request('FullPropertyDetails', variables, '17279788159d9fa5b7ad6c57c7f057714e73d30628a00929c1748d710865f52b')

    variables = {'propertyId': property_id, 'amenitiesInput': {}}  # amenitiesInput is necessary, but we're not currently using the amenities section
    location_scores_resp_json = graphql_request('LocationScoresWithAmenities', variables, '0c752a13cbd06c9b5c5e5ee3323d22ef504f8474664541761feb6f4fad8d9bc0')

    try:
        full_property_details = FullPropertyDetailsResponse(full_details_resp_json).to_dict()
        location_scores = LocationScoresResponse(location_scores_resp_json).to_dict()
        return dict(**full_property_details, **location_scores)
    except Exception as e:
        raise Exception('Unknown error: ' + str(e))


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
    except Exception:
        raise Exception('Unknown error in search ' + resp.text)
    print(search['count'], 'properties found in', round(time() - t, 3), 'seconds')
    return [property['property_id'] for property in search['properties']]


def user_input():
    # Get user input
    location = input('What location do you want to search in (leave blank for Bethlehem): ') or 'Bethlehem, PA'
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


if __name__ == '__main__':
    # user_input()
    d = scrape_property_data('4567308606')
    with open('output.json', 'w') as f:
        json.dump(d, f, indent=4)
