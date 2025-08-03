import re


def camel_to_snake(name: str) -> str:
  """Converts a camelCase string to snake_case."""
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
