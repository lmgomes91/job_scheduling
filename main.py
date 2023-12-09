from src.greedy import Greedy
from src.utils.dataset import open_dataset, format_data


def main():
    data = format_data(open_dataset())
    solver = Greedy()
    solver.run(data)


if __name__ == '__main__':
    main()

