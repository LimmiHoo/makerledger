# === Stage 51: Add unit tests for search and filter behavior ===
# Project: MakerLedger
import unittest

from makerledger.models import Entry, ProjectSnapshot
from makerledger.search import search_entries, filter_by_date_range


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.entries = [
            Entry(id="e1", name="Wood Frame", date="2024-01-15", category="materials"),
            Entry(id="e2", name="Solder Paste", date="2024-02-20", category="consumables"),
            Entry(id="e3", name="Paint Sprayer", date="2024-03-10", category="equipment"),
            Entry(id="e4", name="Copper Wire", date="2024-02-25", category="materials"),
        ]

    def test_search_by_name(self):
        results = search_entries(self.entries, query="Wood")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Wood Frame")

    def test_search_case_insensitive(self):
        results = search_entries(self.entries, query="wood")
        self.assertEqual(len(results), 1)

    def test_search_no_match(self):
        results = search_entries(self.entries, query="xyz")
        self.assertEqual(len(results), 0)

    def test_filter_by_date_range_inclusive(self):
        start, end = "2024-02-20", "2024-03-10"
        results = filter_by_date_range(self.entries, start=start, end=end)
        self.assertEqual(len(results), 2)

    def test_filter_empty_result(self):
        start, end = "2024-05-01", "2024-06-01"
        results = filter_by_date_range(self.entries, start=start, end=end)
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
