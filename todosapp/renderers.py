import humps
from rest_framework.renderers import JSONRenderer


class CamelCaseJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        camelized_data = humps.camelize(data)  # Convert field names to camelCase
        new_data = {"data": camelized_data}
        return super().render(new_data, accepted_media_type, renderer_context)