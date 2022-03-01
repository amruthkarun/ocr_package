#!/usr/bin/env python

"""Tests for `ocr_package` package."""

import unittest

from ocr_package.ocr_package import OCRService


class TestOcr_package(unittest.TestCase):
    """Tests for `ocr_package` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.service = OCRService()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        self.assertEqual(self.service.get_name(), 'Hello')
