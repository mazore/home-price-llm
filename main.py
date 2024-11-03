import csv
import os
from time import sleep
from tqdm import tqdm

from graphql_wrappers import graphql_request, graphql_request_taxes
from setup_logger import setup_logger
from city_data import city_data
from response_handlers import *
from property_search import scrape_property_ids_from_search

logger = setup_logger()

PROPERTIES_PER_CITY = 200  # Number of properties to scrape per city

class APIResponseError(Exception):
    pass


def scrape_property_data(property_id):
    """Takes in a property ID and returns a dictionary with the property data based on the
    realtor.com API. If the property data cannot be scraped, returns None.
    """
    def retry_request(func, *args, retries=3, resp_checker=None):
        for attempt in range(retries):
            response_json = func(*args, logger)

            resp_checked = True
            if resp_checker is not None:
                resp_checked = resp_checker(response_json)

            if response_json is not None and response_json.get('data') is not None and resp_checked:
                return response_json
            logger.warning(f'Error in {func.__name__}, retrying... ({retries - attempt - 1} retries left) Server response: {response_json}')
            sleep(5)
        logger.error(f'Retry failed for {func.__name__}, server response: {response_json}')
        raise APIResponseError(f'Failed to get {func.__name__} after retries')

    try:
        full_details_resp_checker = lambda response_json: response_json.get('data', {}).get('home') is not None
        full_details_resp_json = retry_request(graphql_request, 'FullPropertyDetails', {'propertyId': property_id}, '17279788159d9fa5b7ad6c57c7f057714e73d30628a00929c1748d710865f52b', resp_checker=full_details_resp_checker)
        location_scores_resp_json = retry_request(graphql_request, 'LocationScoresWithAmenities', {'propertyId': property_id, 'amenitiesInput': {}}, '0c752a13cbd06c9b5c5e5ee3323d22ef504f8474664541761feb6f4fad8d9bc0')
        school_data_resp_json = retry_request(graphql_request, 'GetSchoolData', {'propertyId': property_id}, 'ee4267d9cd64801da16099587142fc163d2e04fc6525f2b67924440a90b5f638')
        property_tax_resp_json = retry_request(graphql_request_taxes, property_id)

        return dict(
            property_id=property_id,
            **FullPropertyDetailsResponse(full_details_resp_json).to_dict(),
            **LocationScoresResponse(location_scores_resp_json).to_dict(),
            **SchoolDataResponse(school_data_resp_json).to_dict(),
            **PropertyTaxResponse(property_tax_resp_json).to_dict()
        )
    except APIResponseError as e:
        logger.error(f'API response error while processing property {property_id}: {e}', exc_info=True)
        return None
    except KeyError as e:
        logger.error(f'Missing key error while processing property {property_id}: {e}', exc_info=True)
        return None
    except Exception as e:
        logger.error(f'Unexpected error while processing property {property_id}: {e}', exc_info=True)
        return None


def write_data_to_csv(data, filename, write_header=False):
    with open(filename, 'a', newline='') as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if write_header:  # Write the header only once, at the beginning
            writer.writerow({field: field.replace('_', ' ').title() for field in fieldnames})

        for row in data:
            row_with_null = {k: ("null" if v is None else v) for k, v in row.items()}
            writer.writerow(row_with_null)

    logger.info(f'Saved {len(data)} rows to {filename}')


def scrape_all_cities():
    city_property_data = []
    header_written = False

    try:
        for (state, city_name, _, _) in city_data:
            location = f'{city_name}, {state}'
            logger.info(f'Scraping {PROPERTIES_PER_CITY} properties from {location}...')
            property_ids = scrape_property_ids_from_search(location, PROPERTIES_PER_CITY)
            if len(property_ids) == 0:
                logger.warning(f'No properties found for {location}, skipping...')
                continue

            city_property_data = []
            for property_id in tqdm(property_ids):
                property_data = scrape_property_data(property_id)
                if property_data is None:
                    logger.warning(f'Property {property_id} failed to scrape')
                    continue
                city_property_data.append(property_data)

            write_data_to_csv(city_property_data, 'property_data.csv', write_header=not header_written)
            header_written = True  # Ensure the header is written only once

    except (KeyboardInterrupt, Exception) as e:
        logger.info(f'Received {e}, saving...')
        write_data_to_csv(city_property_data, 'property_data.csv', write_header=not header_written)


if __name__ == '__main__':
    if os.path.exists('property_data.csv'):
        user_input = input("property_data.csv already exists. Do you want to overwrite it? (Y/n): ")
        if user_input.lower() not in ['y', '']:
            logger.info("Exiting without overwriting property_data.csv")
            exit()
        else:
            open('property_data.csv', 'w').close()  # Clear the CSV file

    logger.info(f'Starting scraping {PROPERTIES_PER_CITY} properties per city...')
    scrape_all_cities()

    # For testing
    # d = scrape_property_data('4567308606')
    # with open('scraped_property.json', 'w') as f:
    #     json.dump(d, f, indent=4)
