from ingestion.api_ingestor import ingest_api

def test_ingest_runs():
    config = {
        "source_name": "test",
        "source_type": "api",
        "url": "https://jsonplaceholder.typicode.com/posts",
        "target_path": "bronze/test_api.json"
    }
    ingest_api(config)
    assert open("data/" + config["target_path"]).read()
