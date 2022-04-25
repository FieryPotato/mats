import json
import os
import unittest
from unittest import mock

from src.Reader import Reader

TEST_DATA = {
    'key': 'value',
    'dict 2': {
        'a': 'a',
        'b': 'b'
    }
}


class TestReader(unittest.TestCase):
    path = 'test/MATS.json'

    def setUp(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(TEST_DATA, f)

    def tearDown(self) -> None:
        os.remove(self.path)

    def test_reader_returns_full_path_1(self):
        with mock.patch('src.io._IOManager.path', new_callable=mock.PropertyMock) as p:
            p.return_value = self.path
            actual = Reader().full_path_find('key')
            expected = 'value'
            self.assertEqual(expected, actual)

    def test_reader_returns_full_path_2(self):
        with mock.patch('src.io._IOManager.path', new_callable=mock.PropertyMock) as p:
            p.return_value = self.path
            actual = Reader().full_path_find('dict 2', 'a')
            expected = 'a'
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
