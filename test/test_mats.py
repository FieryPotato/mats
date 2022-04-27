import unittest
from unittest import mock

from src.MATS import MATS


class TestMats(unittest.TestCase):
    def test_add_to_mats(self):
        k = 'glossary', 'ray'
        v = 'A drop of golden sun.'
        inputs = [*k, '', v, '']
        with mock.patch('builtins.input', side_effect=inputs):
            MATS().add_item()
        self.assertEqual(MATS()[k[0]][k[1]], v)


if __name__ == '__main__':
    unittest.main()