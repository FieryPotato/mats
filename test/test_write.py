import json
import os
import unittest
from unittest import mock

from src.MATS import MATS
from src.Writer import Writer
from src.io import _IOManager


TEST_DATA = {
    'glossary': {
        'doe': 'A deer, a female deer.'
    }
}


class TestWriter(unittest.TestCase):
    path = 'test/MATS.json'

    def setUp(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(TEST_DATA, f)
        self.old_path = _IOManager.path
        _IOManager.path = self.path

    def tearDown(self) -> None:
        os.remove(self.path)
        _IOManager.path = self.old_path

    def test_ask_for_keys_as_multi_input(self):
        expected = ['a', 'b', 'c']
        inputs = ['a', 'b', 'c', '']
        with mock.patch('builtins.input', side_effect=inputs):
            keys = Writer().get_keys()
        self.assertEqual(expected, keys)

    def test_ask_for_keys_as_comma_separated_list(self):
        expected = ['a', 'b', 'c']
        inputs = ['a, b, c', '']
        with mock.patch('builtins.input', side_effect=inputs):
            keys = Writer().get_keys()
        self.assertEqual(expected, keys)

    def test_ask_for_value_single_line(self):
        expected = 'Letters'
        inputs = ['Letters', '']
        with mock.patch('builtins.input', side_effect=inputs):
            value = Writer().get_value()
        self.assertEqual(expected, value)

    def test_ask_for_value_multi_line(self):
        expected = 'line 1 line 2'
        inputs = ['line 1', 'line 2', '']
        with mock.patch('builtins.input', side_effect=inputs):
            value = Writer().get_value()
        self.assertEqual(expected, value)

    def test_save_mats(self):
        k = 'mi'
        v = 'A name I call myself.'
        MATS()['glossary'] = {k: v}
        MATS().save()
        with open(self.path) as f:
            data = json.load(f)
        self.assertEqual(data['glossary'][k], v)


if __name__ == '__main__':
    unittest.main()
