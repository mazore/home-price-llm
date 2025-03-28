import csv
import os
from time import sleep
from tqdm import tqdm

from graphql_wrappers import graphql_request, graphql_request_taxes
from setup_logger import setup_logger
from city_data import *
from response_handlers import *
from property_search import scrape_property_ids_from_search

logger = setup_logger()

PROPERTIES_PER_CITY = 240  # Number of properties to scrape per city

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
        def full_details_resp_checker(response_json):
            try:
                home_not_none = response_json.get('data', {}).get('home') is not None
                mortgage_not_none = response_json.get('data', {}).get('home', {}).get('mortgage') is not None
                return home_not_none and mortgage_not_none
            except Exception:
                return False
        full_details_resp_json = retry_request(graphql_request, 'FullPropertyDetails', {'propertyId': property_id}, '8b50ab405dfb496db90affc53a0e846e543dc336e24ba5e63667bfa59fe23dee', resp_checker=full_details_resp_checker)
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
    if data is None:
        return
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
    total_saved_rows = 0
    rows_since_last_sleep = 0

    try:
        for (state, city_name, _, _) in city_data:
            location = f'{city_name}, {state}'
            logger.info(f'Scraping properties from {location}...')
            try:
                property_ids = scrape_property_ids_from_search(location, PROPERTIES_PER_CITY, logger)
            except Exception as e:
                logger.error(f'Failed to scrape properties for {location}: {e}', exc_info=True)
                continue
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

            total_saved_rows += len(city_property_data)
            rows_since_last_sleep += len(city_property_data)  # Increment the counter

            if rows_since_last_sleep >= 2000:
                logger.info(f'Added {rows_since_last_sleep} rows since last sleep (total: {total_saved_rows}), sleeping for 60 seconds...')
                sleep(60)
                rows_since_last_sleep = 0

    except (KeyboardInterrupt, Exception) as e:
        logger.error(f'Received {e}, saving...', exc_info=True)
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
    #d = scrape_property_data('9686105900')
    #write_data_to_csv([d], 'property_data.csv', write_header=False)
    # with open('scraped_property.json', 'w') as f:
    #     json.dump(d, f, indent=4)
