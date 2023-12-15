import csv
import matplotlib.pyplot as plt
import re


def main():
    country = input("Ingresa un país: ")
    read_csv_by_country(country)


def generate_bar_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title(title.capitalize())
    plt.show()


def read_csv_by_country(country):
    labels = []
    values = []

    with open("../documents/world_population.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)
        index_search = header.index("Country/Territory")
        array_countries = list(reader)
        result = list(filter(lambda c: c[index_search] == country.capitalize(), array_countries))

        try:
            if len(result) == 0:
                raise Exception(f"No se encontraron resultados con la palabra ''{country}''.")
            else:
                country_data = list(filter(lambda c: c[index_search] == country.capitalize(), array_countries))[0]
                data = dict(zip(header, country_data))

                for key, value in data.items():
                    if re.match('[0-9]{4} Population', key):
                        labels.append(key.replace(" Population", ""))
                        values.append(int(value))

                generate_bar_chart(labels, values, country)

        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()

