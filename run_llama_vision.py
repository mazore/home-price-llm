import requests
import json
import os
import re
import pandas as pd
import traceback

OPENROUTER_API_KEY = os.environ['OPENROUTER_API_KEY']

TEXT_PROMPT = 'Describe these images. \
Include all descriptions in structured json with only a key "interior" with a string for description of the interior images \
and a key "exterior" with a string for description of the exterior images. \
Include as much detail as possible in your results. Do not produce text besides the JSON. \
Set either to null if not enough detail is provided in the photos.'
# TEXT_PROMPT = """
# The first image is a Google Street View image of the outside of a home. Describe it and give me the description between these two tags: <SV> </SV>.

# The second image is a grid of many images of this home.
# - Describe the images that are of the inside of the home and return the description between these two tags: <IN> </IN>
# - Describe the images that are of the outside of the home and return the description between these two tags: <OUT> </OUT>

# You must include all three tags in your response: <SV> <IN> <OUT>.
# If you are unable to produce meaningful results for any of the tags, you should put "null" in between the tags.
# """


def vision_prompt(street_view_url, grid_url):
    # resp = requests.post(
    #     url="https://openrouter.ai/api/v1/chat/completions",
    #     headers={
    #         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    #     },
    #     data=json.dumps({
    #         "model": "meta-llama/llama-3.2-90b-vision-instruct",
    #         # "model": "meta-llama/llama-3.2-90b-vision-instruct:free",
    #         "temperature": 0,
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": TEXT_PROMPT
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": grid_url
                    }
                }
                # {
                #     "type": "image_url",
                #     "image_url": {
                #         "url": street_view_url
                #     }
                # }
            ]
        }
    ]

    url = "https://api.deepinfra.com/v1/openai/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer gSDWJboQZiy6WjYKRvbGllZJwod2PBG3'
    }
    data = {
        "model": "meta-llama/Llama-3.2-90B-Vision-Instruct",
        "temperature": 0,
        "messages": messages
    }
    resp = requests.post(url, headers=headers, json=data)
    #     })
    # )
    try:
        return resp.json()['choices'][0]['message']['content']
    except:
        return resp.text


STREET_VIEW_URL_TEMPLATE = 'https://home-price-llm.s3.us-east-1.amazonaws.com/{property_id}/street_view.jpg'
GRID_URL_TEMPLATE = 'https://home-price-llm.s3.us-east-1.amazonaws.com/{property_id}/grid.jpg'

def prompt_property(property_id):
    street_view_url = STREET_VIEW_URL_TEMPLATE.format(property_id=property_id)
    grid_url = GRID_URL_TEMPLATE.format(property_id=property_id)
    print('urls:', street_view_url, grid_url)
    return vision_prompt(street_view_url, grid_url), (street_view_url, grid_url)


json_regex = re.compile(
    r'\{\s*"interior"\s*:\s*(?:"([^"]+)"|null)\s*,\s*"exterior"\s*:\s*(?:"([^"]+)"|null)\s*\}',
    re.DOTALL
)


import time
df = pd.read_csv('property_data.csv')
output = []
start_t = time.time()
try:
    for i, row in df.iterrows():
        t = time.time()
        property_id = row['Property Id']
        d = {}
        return_val, urls = prompt_property(property_id)
        d['street_view_url'] = urls[0]
        d['grid_url'] = urls[1]

        match = json_regex.search(return_val)

        # Extracting values if found
        if match:
            interior_value = match.group(1)
            exterior_value = match.group(2)
            d['interior'] = interior_value
            d['exterior'] = exterior_value
            print('got interior value:', interior_value)
            print('got exterior value:', exterior_value)
        else:
            d['interior'] = None
            d['exterior'] = None
            print("No match found", return_val)
        output.append(d)
        print('time:', time.time() - t)
        print('\n\n')
except (KeyboardInterrupt, Exception) as e:
    traceback.print_exc()
finally:
    with open('vision_results.json', 'w') as f:
        json.dump(output, f, indent=4)
    print('total time:', time.time() - start_t, 'for', len(output), 'properties. avg:', (time.time() - start_t) / len(output))
    print('done')
