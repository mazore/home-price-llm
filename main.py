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

def stupid(property_id):
    url = 'https://www.realtor.com/frontdoor/graphql'
    headers = {
        'accept': '*/*',
        'accept-language': 'en,es;q=0.9,es-ES;q=0.8',
        'content-type': 'application/json',
        'cookie': 'split=n; __vst=acae385d-1928-4e05-8ed7-24b4821b46d8; __ssn=0849f17d-c630-4924-b9e1-9056f99664a0; __ssnstarttime=1729567173; __bot=false; _pbjs_userid_consent_data=3524755945110770; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; s_ecid=MCMID%7C67888694234439820254175985671331483854; permutive-id=6fcd21c4-6f6e-4ae3-8bdf-7928ea79645d; _lr_env_src_ats=false; _gcl_au=1.1.324636887.1729567166; pxcts=762be74d-9024-11ef-80b8-b36aa9a052cc; _pxvid=762bdc18-9024-11ef-80b7-c11562e84f68; _cq_duid=1.1729567166.r2gXQzaVNit0HmYP; _cq_suid=1.1729567166.irtlpONVLNPn4vtK; _scid=jz7dXClQmrHi5zj46nKWlJFDmdboyn3a; isAuth0EnabledOnGnav=C1; _ncg_id_=c504670b-6736-4a78-88e1-7d9b5c84c8f4; __split=82; _ncg_domain_id_=c504670b-6736-4a78-88e1-7d9b5c84c8f4.1.1729567205582.1792639205582; _ncg_g_id_=7c063529-9f18-411a-9cc1-0ba19c0bf59f.3.1729567214.1792639205582; _ta=us~1~89df68bc35032d48c293adce8574aa42; _tt_enable_cookie=1; _ttp=-wRt5RlX6IO-9xQZ9iETvHCfbhi; _fbp=fb.1.1729567206829.626053484138208054; __qca=P0-386857228-1729567205305; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; ajs_anonymous_id=89e1c6a2-638c-4dbc-adc1-075881131b50; _cc_id=412d7f1e05ca41a8789be1eb56b71385; mdLogger=false; kampyle_userid=4d7d-7916-fbc4-e567-80ce-cb0b-3a4b-e7a3; G_ENABLED_IDPS=google; ldp-real-estimates=true; ldp-monthly-payment=false; ldp-open-houses=false; _sctr=1%7C1730347200000; leadid_token-27789EFE-7A9A-DB70-BB9B-97D9B7057DBB-01836014-7527-FD48-9B7F-1A40A9705CFE=323590DF-C595-5068-BAFD-655881B0F0AB; _ScCbts=%5B%22565%3Bchrome.2%3A2%3A5%22%2C%22570%3Bchrome.2%3A2%3A5%22%5D; ldp-property-details=false; panoramaId_expiry=1731005736762; panoramaId=7416387425518e6fa730377da66f16d5393809a46112e6816ea369382a1bc35b; _gid=GA1.2.2030309009.1730400935; _lr_geo_location_state=PA; _lr_geo_location=US; _lr_sampling_rate=100; kampylePageLoadedTimestamp=1730400955620; _parsely_session={%22sid%22:7%2C%22surl%22:%22https://www.realtor.com/realestateandhomes-detail/15151-Endicott-St_Philadelphia_PA_19116_M45673-08606%22%2C%22sref%22:%22https://www.google.com/%22%2C%22sts%22:1730405046242%2C%22slts%22:1730400959847}; _parsely_visitor={%22id%22:%22pid=6216b211c84f66a17672a30104955689%22%2C%22session_count%22:7%2C%22last_session_ts%22:1730405046242}; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C20028%7CMCMID%7C67888694234439820254175985671331483854%7CMCAAMLH-1731013934%7C7%7CMCAAMB-1731013934%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1730416334s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; _scid_r=kb7dXClQmrHi5zj46nKWlJFDmdboyn3apWqj3A; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=g%3A8e3b24df-681b-8cab-3296-e1a96cdb2e6c%7Ce%3Aundefined%7Cc%3A1729567165210%7Cl%3A1730409135683; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=g%3Avisitor_acae385d-1928-4e05-8ed7-24b4821b46d8%7Ce%3Aundefined%7Cc%3A1729567165207%7Cl%3A1730409135685; _rdt_uuid=1729567166647.2318816c-95d0-413b-8e5a-8f0d2986b66f; split_tcv=133; _ncg_sp_ses.cc72=*; _ncg_sp_id.cc72=c504670b-6736-4a78-88e1-7d9b5c84c8f4.1729567206.7.1730409137.1730401004.552191ef-8a6a-4ce5-b91a-e46d8467bd00; _tac=false~google|not-available; _tas=6iq6gknn6r; cto_bundle=4N7na19qY3UlMkJYUFNYRUxGdnV1NE1VUFRZQktTRDhScUg5T3NKOGFnaTRIVU5yMkJ3dEslMkZSOXRYcDU1MHE0M2hCV0x5U0VpMDVnYUlDRldocU9vZFR3eEM3SUgxJTJCR3ZseEJMUlFBM29hME5nbklLS2pEZyUyQnglMkJyQkpPMEg1YlVyUnR0OCUyQmJYUUVkR1dSS05sMHYlMkI4WFVWUnYlMkJjM25ER2N1eXFsa2Q2dmx0ZnhzMjVGeFd5dENaSEZYVHNRZFFqbDdseWlIZ3lEOXJPQkh2TGF1SjBNcmtxJTJCaEwyanhldFp2VkNrM0tYaW9ZY3BZaFRaYnlWdzk4dGw5JTJCMnkxS1AzV1pKTHA; cto_bundle=4N7na19qY3UlMkJYUFNYRUxGdnV1NE1VUFRZQktTRDhScUg5T3NKOGFnaTRIVU5yMkJ3dEslMkZSOXRYcDU1MHE0M2hCV0x5U0VpMDVnYUlDRldocU9vZFR3eEM3SUgxJTJCR3ZseEJMUlFBM29hME5nbklLS2pEZyUyQnglMkJyQkpPMEg1YlVyUnR0OCUyQmJYUUVkR1dSS05sMHYlMkI4WFVWUnYlMkJjM25ER2N1eXFsa2Q2dmx0ZnhzMjVGeFd5dENaSEZYVHNRZFFqbDdseWlIZ3lEOXJPQkh2TGF1SjBNcmtxJTJCaEwyanhldFp2VkNrM0tYaW9ZY3BZaFRaYnlWdzk4dGw5JTJCMnkxS1AzV1pKTHA; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCMID%7C67888694234439820254175985671331483854%7CMCIDTS%7C20028%7CMCOPTOUT-1730416337s%7CNONE%7CvVersion%7C5.2.0; adcloud={%22_les_v%22:%22c%2Cy%2Crealtor.com%2C1730410937%22}; __gads=ID=a068e5c758756119:T=1729567216:RT=1730409141:S=ALNI_MYkUXRjgumv8VzqliWRFlKFd6VnqA; __gpi=UID=00000f2f68b5d848:T=1729567216:RT=1730409141:S=ALNI_MYJl3uVdi0LVGxGf0WkOmTP7u0Ruw; __eoi=ID=bd276937f40f5f72:T=1729567216:RT=1730409141:S=AA-Afjbmz8-icP9wuWeP1T4Z1dx_; _ga=GA1.2.729855264.1729567207; cto_bundle=bLm1_F9qY3UlMkJYUFNYRUxGdnV1NE1VUFRZQkxzUmFSMFNHRjdmWGlFeGhlZFlCOVN0Tm9GRks2cDA5ZUVyekolMkZ3YnVLdE01NVZvRGFvYnBQWUlQT3BlQW1GNE41JTJGTldJYmVQWnVRQk1BaXNyZ2tuc3pzbnpkaTd6TEpmNFpETGdXenRjaUdyMmRnV1RSWGg4U1RVYTB1RU43dnVBVCUyQmEwbWFPRWJacjk4OXhwVDM1MFQwQU9nSHVnUlVkV1hBU2xIazl1bG5KemdkUlA3JTJCaiUyQjExMWkwYjlqZXRVNiUyQjhDZ1g1M0FMSklVMXFBTnFocW5QNWRzWGt3Q0NXYUhYbWJPSE1vZVE; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=g%3A81c56785-645f-fb2b-56c8-c76629a81e36%7Ce%3A1730410943215%7Cc%3A1730409135680%7Cl%3A1730409143215; kampyleUserSession=1730409143650; kampyleUserSessionsCount=7; kampyleSessionPageCounter=1; kampyleUserPercentile=16.305083347085336; ldp-neighborhood=true; ldp-property-history=false; _gat=1; _uetsid=b6742aa097b911efb5160941c9edade0|3d6fh7|2|fqh|0|1765; _uetvid=8a374760902411efa01dfd28267fded6|nvrwn5|1730409645406|5|1|bat.bing.com/p/insights/c/v; _ga_MS5EHT6J6V=GS1.1.1730409138.8.1.1730409652.58.0.0',
        'origin': 'https://www.realtor.com',
        'priority': 'u=1, i',
        'rdc-client-name': 'RDC_WEB_DETAILS_PAGE',
        'rdc-client-version': '2.1.45',
        'referer': 'https://www.realtor.com/realestateandhomes-detail/15151-Endicott-St_Philadelphia_PA_19116_M45673-08606',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-is-bot': 'false'
    }
    data = '{"operationName":"PropertyAndTaxHistory","variables":{"propertyId":"' + property_id + '"},"query":"query PropertyAndTaxHistory($propertyId: ID\u0021) {\\n  home(property_id: $propertyId) {\\n    status\\n    property_history {\\n      date\\n      event_name\\n      price\\n      price_change\\n      price_sqft\\n      source_listing_id\\n      source_name\\n      price_change_percentage\\n      days_after_listed\\n      listing {\\n        list_price\\n        last_status_change_date\\n        last_update_date\\n        status\\n        list_date\\n        listing_id\\n        __typename\\n      }\\n      __typename\\n    }\\n    tax_history {\\n      assessment {\\n        building\\n        land\\n        total\\n        __typename\\n      }\\n      market {\\n        building\\n        land\\n        total\\n        __typename\\n      }\\n      tax\\n      year\\n      __typename\\n    }\\n    __typename\\n  }\\n}"}'
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
    property_tax_resp_json = stupid(property_id)

    try:
        return dict(
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
    user_input()
    # d = scrape_property_data('4716766863')
    # with open('scraped_property.json', 'w') as f:
    # with open('output.json', 'w') as f:
    #     json.dump(d, f, indent=4)
