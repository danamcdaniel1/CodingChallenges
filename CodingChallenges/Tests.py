import unittest

from CodingChallenges.DirPrint import print_directory_contents
from CodingChallenges.StringCompressor import unique_char_counts, run_length_encoding


class Test_DirPrint(unittest.TestCase):

    def test_3(self):
        # this directory contains three presentation files
        counter = 0
        for file in print_directory_contents(r"C:\Users\mcdanid2\Desktop\ADQC Brown Bag"):
            counter += 1
        self.assertEqual(counter, 3)


    def test_HCP(self):
        # this directory contains 6 top level MS files and workflows + 2 top level directories:
        # byos_tmp; test_HC_project.blgc.presets
        counter = 0
        for file in print_directory_contents(r"C:\Users\mcdanid2\Desktop\HCP"):
            counter += 1
        print("There are " + str(counter) + " files here.")
        self.assertEqual(counter, 60)

class Test_StringCompressor(unittest.TestCase):

    def test_unique_char_counts(self):
        self.assertEqual(unique_char_counts("ABCACB"), "A2B2C2")

    def test_run_length_encoding(self):
        self.assertEqual(run_length_encoding("AAABBBAAA"), "A3B3A3") # compressed shorter than string
        self.assertEqual(run_length_encoding("AABBAAA"), "A2B2A3") # equal size string and compressed
        self.assertEqual(run_length_encoding("bookkeeper"), "bookkeeper") # string shorter than compressed



if __name__ == '__main__':
    unittest.main()