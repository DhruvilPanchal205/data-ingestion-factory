import requests, os, json

def ingest_api(config):
    print(f"Ingesting: {config['url']}")
    response = requests.get(config['url'])
    text = response.text.lstrip('jsonFlickrFeed(').rstrip(')')
    data = json.loads(text)
    
    os.makedirs("data/" + os.path.dirname(config["target_path"]), exist_ok=True)
    with open("data/" + config["target_path"], "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved to: data/{config['target_path']}")
