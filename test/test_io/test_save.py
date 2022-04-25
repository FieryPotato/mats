import json
import os
import unittest
from unittest.mock import patch, PropertyMock

from src.io import IOManager


class TestSave(unittest.TestCase):
    def test_save_mats(self):
        data = {'key': 'value'}
        with file_write_cm() as cm:
            with patch('src.io._IOManager.mats_path', new_callable=PropertyMock) as mock:
                mock.return_value = cm.path
                IOManager().save_mats(data)
                with open(cm.path) as file:
                    self.assertEqual(data, json.load(file))


class file_write_cm:
    path = 'test\\test_io\\test_write.json'

    def __enter__(self):
        f = open(self.path, 'w')
        f.write('{}')
        f.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)


if __name__ == '__main__':
    unittest.main()
