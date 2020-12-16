from utils.console_utility import menu
import src.load_data as load_data
import src.mock_data as mock_data

print(menu())
while True:
    operacja = input("Co wybierzesz? ")
    if operacja == "1":
        print(":::Podaj:::\n"), load_data.main()
    elif operacja == "2":
        print(":::Przykładowe dane:::\n"), mock_data.main()
    elif operacja == "0":
        print(menu())
    else:
        break
