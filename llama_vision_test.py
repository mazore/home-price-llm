import requests
import json

OPENROUTER_API_KEY = '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'


def vision_prompt(image_url):
    resp = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.2-90b-vision-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Describe this image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ]
        })
    )
    try:
        return resp.json()['choices'][0]['message']['content']
    except:
        return resp.text


if __name__ == '__main__':
    print(vision_prompt('https://ap.rdcpix.com/22eda16690e45a91664c62ca358d263el-m24665339rd-w960_h720.webp'))
