import os
import requests
import json
import re

# Load config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'patent_sources.json')
with open(config_path) as f:
    sources = json.load(f)

for source in sources:
    url = source["url"]
    file_name = f"{source['source_name']}.json"

    print(f"Fetching from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Flickr returns JSONP — we must clean it
        raw_text = response.text
        # Strip jsonFlickrFeed(...) wrapper
        json_text = re.sub(r'^jsonFlickrFeed\((.*)\)$', r'\1', raw_text.strip(), flags=re.DOTALL)

        data = json.loads(json_text)
        print(f"Fetched {len(data.get('items', []))} items.")
    except Exception as e:
        print(f"Error: {e}")
        continue

    # Save to data folder
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to: {file_path}")
