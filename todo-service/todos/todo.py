from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
import json

from jsontools.encoder import Encoder

@dataclass
class Todo:
    id: UUID = None
    user_id: UUID = None
    title: str = ""
    completed: bool = False
    created_at: datetime = datetime.now()

    def to_json(self) -> str:
        return json.dumps(self.__dict__, cls=Encoder, ensure_ascii=False)

    @classmethod
    def from_json(todo, json_str):
        json_dict = json.loads(json_str)
        return todo(**json_dict)
