import json
import requests

with open('../../api/huggingface_api.txt','r') as f:
    API_key = f.read()
headers = {f"Authorization": f"Bearer {API_key}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

# file_name = 'recorded_audio.flac'
def query(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

