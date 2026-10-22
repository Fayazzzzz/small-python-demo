"""Tests for the greeting, validation, and store modules."""

import unittest

from service.greeting import greet
from service.store import GreetingStore
from service.validators import is_valid_name


class ValidatorTests(unittest.TestCase):
    def test_accepts_letters_and_spaces(self) -> None:
        self.assertTrue(is_valid_name("Ada Lovelace"))

    def test_rejects_empty_and_digits(self) -> None:
        self.assertFalse(is_valid_name("   "))
        self.assertFalse(is_valid_name("Ada1"))


class GreetTests(unittest.TestCase):
    def test_greets_trimmed_name(self) -> None:
        self.assertEqual(greet("  Ada "), "Hello, Ada!")

    def test_rejects_invalid_name(self) -> None:
        with self.assertRaises(ValueError):
            greet("")


class StoreTests(unittest.TestCase):
    def test_keeps_each_name_once_in_order(self) -> None:
        store = GreetingStore()
        store.record("Ada")
        store.record("Grace")
        store.record("Ada")
        self.assertEqual(store.names(), ["Ada", "Grace"])


if __name__ == "__main__":
    unittest.main()
