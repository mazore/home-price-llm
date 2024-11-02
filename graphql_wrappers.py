import json
import requests

def graphql_request(operation_name, variables, sha_hash, logger):
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

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        return resp.json()
    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        logger.error(f"Network error during GraphQL request: {e}")
        return None

def graphql_request_taxes(property_id, logger):
    url = 'https://www.realtor.com/frontdoor/graphql'
    headers = {
        'content-type': 'application/json',
        'rdc-client-name': 'RDC_WEB_DETAILS_PAGE',
        'rdc-client-version': '2.1.6',
    }
    # Should be turned into a dictionary and cleaned up
    data = '{"operationName":"PropertyAndTaxHistory","variables":{"propertyId":"' + property_id + '"},"query":"query PropertyAndTaxHistory($propertyId: ID) { home(property_id: $propertyId) { status property_history { date event_name price price_change price_sqft source_listing_id source_name price_change_percentage days_after_listed listing { list_price last_status_change_date last_update_date status list_date listing_id __typename } __typename } tax_history { assessment { building land total __typename } market { building land total __typename } tax year __typename } __typename }}"}'
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        logger.error(f"Network error during GraphQL request: {e}")
        return None
