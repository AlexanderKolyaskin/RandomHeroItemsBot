import json
from config.models import Settings

def read_config():
    with open(".config/items.json", "r", encoding="utf-8") as f:
        data = f.read()
        return Settings.from_json(data)