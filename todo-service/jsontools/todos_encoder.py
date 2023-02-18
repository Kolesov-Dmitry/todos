import json

from todos.todo import Todo

class Encoder(json.JSONEncoder):
    def default(self, obj) -> str:        
        if isinstance(obj, Todo):
            return obj.to_json()

        return json.JSONEncoder.default(self, obj)
