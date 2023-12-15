import csv
import matplotlib.pyplot as plt


def main():
    with open("../documents/world_population.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        result = [element for element in list(reader) if element[4] == "South America"]

        percentages = [element[-1] for element in result]
        countries = [element[2] for element in result]

        generate_pie_chart(countries, percentages)


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()


if __name__ == '__main__':
    main()

