from src.binary_search import binary_search


def main():
    arr = [10, 22, 27, 80, 115, 190, 225]
    print("Tablica: ", arr)
    result_index = binary_search(arr, 80)
    print("Szukam liczby 80... Jest na indeksie  ", result_index)


if __name__ == "__main__":
    main()