
import csv
from src.Fileutilities.absolutepath import absolute_path


#def class_factory(class_name, dictionary):
    #return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self):
        pass

    def __init__(self, filepath):
        with open(filepath, 'r') as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        if not self.data:
            raise Exception('List is empty.')
        else:
            return self.data