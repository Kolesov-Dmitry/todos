import json
from uuid import UUID
from datetime import date, datetime

class Encoder(json.JSONEncoder):
    def default(self, obj) -> str:
        if isinstance(obj, UUID):
            return obj.hex
        
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)
