import json
from ingestion.api_ingestor import ingest_api

with open("configs/patent_sources.json") as f:
    jobs = json.load(f)

for job in jobs:
    if job["source_type"] == "api":
        ingest_api(job)
