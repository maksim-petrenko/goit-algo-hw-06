# GoIT
# Python Data Science and Machine Learning Course
# Module 06
# Homework
# Copyright (C) 2026 Maksim Petrenko


"""Address book management system."""


__all__ = ("AddressBook",
           "Record")


# Standard library
from collections import UserDict


# Constants
# Table
TABLE_LINE = "+--------------------------+--------------+\n"
TABLE_ROW = "| {0:24} | {1:12} |\n"
TABLE_HEAD = (TABLE_LINE + TABLE_ROW.format("Contact name", "Phone number")
              + TABLE_LINE)


########################################################################
# Internal classes


class Field():
    """Internal class. Base class for record fields."""
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

    def __eq__(self, obj) -> bool:
        if isinstance(obj, Field):
            return self.value == obj.value
        if isinstance(obj, str):
            return self.value == obj


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


class Record():
    """Class for storing contact information."""
    # Quick initialization.
    # For example:
    #>>> john_record = Record("John", "1234567890")
    def __init__(self, name: str, phone: str = "") -> None:
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def __repr__(self) -> str:
        return "Record(name={}, phones={})".format(self.name, self.phones)

    def add_phone(self, phone: str) -> None:
        """Implements the "add" command."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """Internal method."""
        self.phones.remove(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Implements the "change" command."""
        index = self.phones.index(Phone(old_phone))
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        """Internal method."""
        target = Phone(phone)
        if target in self.phones:
            return target


class AddressBook(UserDict):
    """Class for storing and managing records."""
    # Pretty print is performed by the handler.
    def __str__(self) -> str:
        table = TABLE_HEAD
        for name in sorted(self):
            for phone in self.get(name).phones:
                table += TABLE_ROW.format(name, phone.value)
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
