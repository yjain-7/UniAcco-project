import csv
import argparse

class CSVTool:
    def __init__(self):
        self.data = None

    def load(self, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            self.data = [row for row in reader]

    def count(self):
        return len(self.data)

    def mean(self, column):
        col_data = [float(row[column]) for row in self.data]
        return sum(col_data) / len(col_data)

    def filter(self, column, value):
        return [row for row in self.data if row[column] == value]
    
    def print(self):
        print(self.data, sep = "/n")
    
    def sort_by_column(self, column):
        with open('sorted.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames = self.data[0].keys())
            writer.writeheader()
            writer.writerows(sorted(self.data, key = lambda row: float(row[column])))

    def std_dev(self, column):
        col_data = [float(row[column]) for row in self.data]
        mean = self.mean(column)
        return (sum([(x - mean) ** 2 for x in col_data]) / len(col_data)) ** 0.5

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='CSV file to load')
    args = parser.parse_args()

    tool = CSVTool()

    tool.load(args.file)

    while True:
        command = input('> ')

        if command.startswith('count'):
            print(tool.count())

        elif command.startswith('mean'):
            column = command.split()[1]
            print(tool.mean(column))

        elif command.startswith('filter'):
            column, value = command.split()[1:]
            print(tool.filter(column, value))

        elif command.startswith('exit'):
            break
        
        elif command.startswith('sort'):
            column = command.split()[1]
            tool.sort_by_column(column)
        
        elif command.startswith('print'):
            tool.print()
        
        elif command.startswith('std_dev'):
            column = command.split()[1]
            print(tool.std_dev(column))

        else:
            print("Invalid command")
            

if __name__ == '__main__':
    main()
