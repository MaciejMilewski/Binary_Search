def binary_search(sorted_arr, wanted_num):
    """ Szuka elementu w posortwanej tablicy, jeżeli znajdzie to zwraca indeks szukanego elementu. W przypadku nie znalezienia elemetu zwraca -1."""
    left = 0
    right = len(sorted_arr) - 1
    mid = 0

    while left <= right:
        mid = (right + left) // 2
        if sorted_arr[mid] < wanted_num:
            left = mid + 1
        elif sorted_arr[mid] > wanted_num:
            right = mid - 1
        else:
            return mid
    return -1
