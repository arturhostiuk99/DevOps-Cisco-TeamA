import unittest
import subprocess


class TestMain(unittest.TestCase):

    def test_find_file_1(self):
        command = "python main.py test find"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn('file1.txt', result, 'Wrong file')

    def test_find_file_2(self):
        command = "python main.py test file"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn('file2.txt', result, 'Wrong file')

    def test_find_file_both(self):
        command = "python main.py test some"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn('file1.txt', result, 'Wrong file')
        self.assertIn('file2.txt', result, 'Wrong file')

    def test_find_file_none(self):
        command = "python main.py test none"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn('No match found', result, 'Result should not contain files')


if __name__ == '__main__':
    unittest.main()
