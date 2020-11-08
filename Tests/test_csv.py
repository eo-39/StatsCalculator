import unittest

from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.datafile = CsvReader()

    def test_instantiate_parser(self):
        self.assertIsInstance(self.datafile, CsvReader)

  #  def test_file_parser(self):
     #   filepath = './Tests/Data/Unit Test Addition.csv'
     #   file_data = self.datafile.csv(filepath)

#        for row in file_data:
#            print(row)
#        file_data.clear()

    def test_empty_list(self):
       #Empty list
       #filepath = './Tests/Data/Unit Test Empty.csv'
       #Non-Empty List
       filepath = './Tests/Data/Unit Test Addition.csv'

       file_data = self.datafile.csv(filepath)
       # for row in file_data:
       #     print(row)
       file_data.clear()


if __name__ == '__main__':
    unittest.main()