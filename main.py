from src.utils.dataset import open_dataset


def main():
    df = open_dataset()
    print(df.head())


if __name__ == '__main__':
    main()

