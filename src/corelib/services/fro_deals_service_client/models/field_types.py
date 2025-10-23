from enum import Enum


class FieldTypes(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    ENUM = "enum"
    FLOAT = "float"
    INTEGER = "integer"
    JSON = "json"
    STRING = "string"
    TIME = "time"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
