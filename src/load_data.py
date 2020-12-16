from src.binary_search import binary_search


def main():
    given_array_length = int(input("Długość tablicy: "))
    given_array = list(map(int, input("\nLiczny do tablicy: ").strip().split()))[:given_array_length]
    wanted_number = int(input("Szukany element: "))

    given_array.sort()

    result_index = binary_search(given_array, wanted_number)
    print("Szukam liczby ", wanted_number, "... Jest na indeksie  ", result_index)


if __name__ == "__main__":
    main()