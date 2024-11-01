import csv
import json
import requests
from response_handlers import *
from property_search import scrape_property_ids_from_search
from time import time
import traceback

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

def graphql_request_taxes(property_id):
    url = 'https://www.realtor.com/frontdoor/graphql'
    headers = {
        'content-type': 'application/json',
        'rdc-client-name': 'RDC_WEB_DETAILS_PAGE',
        'rdc-client-version': '2.1.6',
    }
    # Should be turned into a dictionary
    data = '{"operationName":"PropertyAndTaxHistory","variables":{"propertyId":"' + property_id + '"},"query":"query PropertyAndTaxHistory($propertyId: ID) { home(property_id: $propertyId) { status property_history { date event_name price price_change price_sqft source_listing_id source_name price_change_percentage days_after_listed listing { list_price last_status_change_date last_update_date status list_date listing_id __typename } __typename } tax_history { assessment { building land total __typename } market { building land total __typename } tax year __typename } __typename }}"}'
    response = requests.post(url, headers=headers, data=data)
    return response.json()


def scrape_property_data(property_id):
    """Takes in a property ID and returns a dictionary with the price, address, photo URL, and
    description of the house based on the realtor.com API. This can easily be adjusted to include
    square footage, number of bedrooms, etc.
    """
    variables = {'propertyId': property_id}
    full_details_resp_json = graphql_request('FullPropertyDetails', variables, '17279788159d9fa5b7ad6c57c7f057714e73d30628a00929c1748d710865f52b')

    variables = {'propertyId': property_id, 'amenitiesInput': {}}  # amenitiesInput is necessary, but we're not currently using the amenities section
    location_scores_resp_json = graphql_request('LocationScoresWithAmenities', variables, '0c752a13cbd06c9b5c5e5ee3323d22ef504f8474664541761feb6f4fad8d9bc0')

    variables = {'propertyId': property_id}
    school_data_resp_json = graphql_request('GetSchoolData', variables, 'ee4267d9cd64801da16099587142fc163d2e04fc6525f2b67924440a90b5f638')

    variables = {'propertyId': property_id}
    property_tax_resp_json = graphql_request_taxes(property_id)

    try:
        return dict(
            property_id=property_id,
            **FullPropertyDetailsResponse(full_details_resp_json).to_dict(),
            **LocationScoresResponse(location_scores_resp_json).to_dict(),
            **SchoolDataResponse(school_data_resp_json).to_dict(),
            **PropertyTaxResponse(property_tax_resp_json).to_dict()
        )
    except Exception as e:
        traceback.print_exc()
        return


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
        if property_data is None:
            print(f'Property {i + 1} of {len(property_ids)} failed to scrape, property ID: {property_id}')
            continue
        print(f'Property {i + 1} of {len(property_ids)} scraped in', round(time() - t, 3), 'seconds')
        all_property_data.append(property_data)
        # break

    # Write to CSV
    with open('property_data.csv', 'w', newline='') as f:
        fieldnames = list(all_property_data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerow({field: field.replace('_', ' ').title() for field in fieldnames})

        # writer.writerows(all_property_data)
        for row in all_property_data:
            row_with_null = {k: ("null" if v is None else v) for k, v in row.items()}
            writer.writerow(row_with_null)


if __name__ == '__main__':
    # user_input()
    d = scrape_property_data('4567308606')
    with open('scraped_property.json', 'w') as f:
    # with open('output.json', 'w') as f:
        json.dump(d, f, indent=4)
