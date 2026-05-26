# GoIT
# Python Data Science and Machine Learning Course
# Module 06
# Homework
# Copyright (C) 2026 Maksim Petrenko


"""Address book management system."""


__all__ = ("AddressBook",
           "Record")


# Standard library
from collections import UserDict, UserString


# Constants
# Table
TABLE_LINE = "+--------------------------+--------------+\n"
TABLE_ROW = "| {0:24} | {1:12} |\n"
TABLE_HEAD = (TABLE_LINE + TABLE_ROW.format("Contact name", "Phone number")
              + TABLE_LINE)


########################################################################
# Internal classes


class Field(UserString):
    """Internal class. Base class for record fields."""
    def __init__(self, value: str) -> None:
        super().__init__(value)
        self.value = value


class Name(Field):
    """Internal class. Class for storing the contact name."""
    # Name validation is performed by the handler.
    pass


class Phone(Field):
    """Internal class. Class for storing a phone number."""
    # Phone validation is performed by the handler.
    def __init__(self, value: str) -> None:
        if not (value.isdigit() and len(value) == 10):
            raise ValueError
        super().__init__(value)


########################################################################
# Public classes


class Record(UserDict):
    """Class for storing contact information."""
    # Quick initialization.
    # For example:
    #>>> john_record = Record("John", "1234567890")
    #>>> john_record
    #{'name': 'John', 'phones': ['1234567890']}
    def __init__(self, name: str, phone: str = "") -> None:
        phones = [Phone(phone)] if phone else []
        super().__init__({"name": Name(name), "phones": phones})
        self.name = Name(name)
        self.phones = phones

    # Instance methods wrap superclass methods.

    def add_phone(self, phone: str) -> None:
        """Implements the "add" command."""
        self.get("phones").append(Phone(phone))
        self.phones = self.get("phones")

    def remove_phone(self, phone: str) -> None:
        """Internal method."""
        self.get("phones").remove(Phone(phone))
        self.phones = self.get("phones")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Implements the "change" command."""
        #>>> john_record = Record("John", "1234567890")
        #>>> john_record.edit_phone("111", "333")
        #ValueError
        index = self.get("phones").index(Phone(old_phone))
        self.get("phones")[index] = Phone(new_phone)
        self.phones = self.get("phones")

    def find_phone(self, phone: str) -> Phone | None:
        """Internal method."""
        target = Phone(phone)
        for number in self.get("phones"):
            if number == target:
                return number


class AddressBook(UserDict):
    """Class for storing and managing records."""
    # Pretty print is performed by the handler.
    def __str__(self) -> str:
        table = TABLE_HEAD
        for name in sorted(self):
            for phone in self.get(name).get("phones"):
                table += TABLE_ROW.format(name, phone.data)
        table += TABLE_LINE
        return table

    # Instance methods wrap superclass methods.

    def add_record(self, record: Record) -> None:
        """Implements the "add" command."""
        self.update({record.name.value: record})

    def find(self, name: str) -> Record | None:
        """Internal method."""
        return self.get(name)

    def delete(self, name: str) -> None:
        """Internal method."""
        self.pop(name)
