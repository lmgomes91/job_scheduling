from src.greedy import Greedy
from src.sequential_no_specify import Sequential
from src.utils.dataset import open_dataset, format_data, format_data_no_machine_specify


def main():
    data = format_data(open_dataset())
    solver = Greedy()
    solver.run(data)

    data = format_data_no_machine_specify(open_dataset())
    solver = Sequential(5, 5, 1)
    solver.run(data)


if __name__ == '__main__':
    main()

