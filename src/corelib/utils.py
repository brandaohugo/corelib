import re
from fastapi.routing import APIRoute


def custom_generate_unique_id(route: APIRoute) -> str:
    tag = route.tags[0] if route.tags else "untagged"
    return f"{tag}-{route.name}"


def camel_to_snake(name: str) -> str:
  """Converts a camelCase string to snake_case."""
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
