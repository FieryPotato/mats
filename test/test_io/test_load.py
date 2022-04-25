import unittest
from unittest.mock import patch

from src.io import mats_path, load_mats


class TestLoad(unittest.TestCase):

    def test_loader_target_file(self):
        path = "data/MATS.json"
        self.assertEqual(path, mats_path)

    def test_loader_opens_json(self):
        data = {"key", "value"}
        with patch("json.load", return_value=data):
            self.assertEqual(data, load_mats())


if __name__ == '__main__':
    unittest.main()
