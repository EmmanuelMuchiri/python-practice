import unittest
import readfiles


class TestReadFiles(unittest.TestCase):
    def test_get_data(self):
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file("test.txt"))

    def test_nonfile(self):

        self.assertEqual(None, readfiles.read_file("tests.txt"))

        try:
            with open(text_file, "r") as handle:

                data = handle.read()
                return data
        except FileNotFoundError:

            return None


if __name__ == "__main__":
    unittest.main()
