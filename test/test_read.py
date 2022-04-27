import json
import os
import unittest

from src.MATS import MATS
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
    def setUp(self) -> None:
        MATS().update(TEST_DATA)

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

    def test_reader_queries_mats(self):
        k = ['glossary', 'fa']
        v = 'A long, long way to run'
        MATS()[k[0]][k[1]] = v
        expected = v
        actual = Reader().full_path_find(*k)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
