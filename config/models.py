from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Item:
    name: str
    category: str
    partOf: list[str]
    img_path: str

@dataclass_json
@dataclass
class Settings:
    token: str
    Heroes: list[str]
    Items: list[Item]
