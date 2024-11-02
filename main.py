import csv
import json
import requests
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
    def retry_request(func, *args, retries=3):
        for attempt in range(retries):
            response_json = func(*args, logger)
            if response_json is not None and response_json.get('data') is not None:
                return response_json
            logger.warning(f'Error in {func.__name__}, retrying... ({retries - attempt - 1} retries left) Server response: {response_json}')
            sleep(5)
        logger.error(f'Retry failed for {func.__name__}, server response: {response_json}')
        raise APIResponseError(f'Failed to get {func.__name__} after retries')

    try:
        full_details_resp_json = retry_request(graphql_request, 'FullPropertyDetails', {'propertyId': property_id}, '17279788159d9fa5b7ad6c57c7f057714e73d30628a00929c1748d710865f52b')
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


def write_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerow({field: field.replace('_', ' ').title() for field in fieldnames})

        # writer.writerows(all_property_data)
        for row in data:
            row_with_null = {k: ("null" if v is None else v) for k, v in row.items()}
            writer.writerow(row_with_null)
    logger.info(f'Saved {len(data)} rows to {filename}')


def scrape_all_cities():
    all_property_data = []

    try:
        for (state, city_name, _, _) in city_data:
            location = f'{city_name}, {state}'
            logger.info(f'Scraping {PROPERTIES_PER_CITY} properties from {location}...')
            property_ids = scrape_property_ids_from_search(location, PROPERTIES_PER_CITY)
            if len(property_ids) == 0:
                logger.warning(f'No properties found for {location}, skipping...')
                continue

            # Get property data for each property
            for property_id in tqdm(property_ids):
                property_data = scrape_property_data(property_id)
                if property_data is None:
                    logger.warning(f'Property {property_id} failed to scrape')
                    continue
                all_property_data.append(property_data)

            logger.info(f"Saving backup of {len(all_property_data)} records.")
            write_data_to_csv(all_property_data, 'property_data_backup.csv')

        write_data_to_csv(all_property_data, 'property_data.csv')

    except (KeyboardInterrupt, Exception) as e:
        logger.info(f'Received {e}, saving...')
        write_data_to_csv(all_property_data, 'property_data.csv')


if __name__ == '__main__':
    logger.info(f'Starting scraping {PROPERTIES_PER_CITY} properties per city...')
    scrape_all_cities()

    # For testing
    # d = scrape_property_data('4567308606')
    # with open('scraped_property.json', 'w') as f:
    #     json.dump(d, f, indent=4)
