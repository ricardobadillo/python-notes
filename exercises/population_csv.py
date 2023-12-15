import csv


def read_csv(file):
    with open("../documents/world_population.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)

        result = [(dict(zip(header, element))) for counter, element in enumerate(reader) if counter <= 2]
        return result


if __name__ == '__main__':
    data = read_csv("../documents/world_population.csv")
    print(data)


"""
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv("../documents/world_population.csv")
  print(data[0])
"""