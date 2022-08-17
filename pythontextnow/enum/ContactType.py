from enum import unique, Enum


@unique
class ContactType(Enum):
    DEFAULT = 1
    MEDIA = 2
