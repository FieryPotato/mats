import json
import os
import unittest

from src.io import _IOManager
from src.Reader import Reader, pathify

TEST_DATA = {
    'key': 'value',
    'dict 2': {
        'a': 'a',
        'b': 'b'
    },
    'second key': {
        'hidden value': 'value',
        'unknown path': 'path'
    },
    'glossary': {
        'pikachu': 'It keeps its tail raised to monitor its surroundings. '
                   'If you yank its tail, it will try to bite you.'
    }
}


class TestReader(unittest.TestCase):
    path = 'test/MATS.json'

    def setUp(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(TEST_DATA, f)
        self.old_path = _IOManager.path
        _IOManager.path = self.path

    def tearDown(self) -> None:
        os.remove(self.path)
        _IOManager.path = self.old_path

    def test_reader_returns_full_path_1(self):
        actual = Reader().full_path_find('key')
        expected = 'value'
        self.assertEqual(expected, actual)

    def test_reader_returns_full_path_2(self):
        actual = Reader().full_path_find('dict 2', 'a')
        expected = 'a'
        self.assertEqual(expected, actual)

    def test_reader_checks_recursively_on_key_error(self):
        actual = Reader().full_path_find('pikachu')
        expected = [('glossary',
                     'pikachu',
                     'It keeps its tail raised to monitor its surroundings. '
                     'If you yank its tail, it will try to bite you.')]
        self.assertEqual(expected, actual)

    def test_reader_gets_all_results_with_key_error(self):
        actual = Reader().full_path_find('value')
        expected = [('key', 'value'), ('second key', 'hidden value', 'value')]
        self.assertEqual(expected, actual)

    def test_reader_formats_paths(self):
        full_paths = Reader().full_path_find('path')
        actual = [pathify(path) for path in full_paths]
        expected = ["MATS > second key > unknown path > path"]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
