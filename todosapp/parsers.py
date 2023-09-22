import humps
from rest_framework import exceptions
from rest_framework.parsers import JSONParser


class CustomJSONParser(JSONParser):
    def parse(self, stream, media_type=None, parser_context=None):
        try:
            data = super().parse(stream, media_type, parser_context)
            
            # Check if the "data" key is present in the JSON data
            if "data" in data:
                data = data["data"]
            
            # Decamelize the keys in the data
            decamelized_data = humps.decamelize(data)
            
            return decamelized_data
        except Exception as exc:
            raise exceptions.ParseError(f"JSON parse error - {str(exc)}")
