from lab1 import identlims

def test_sklad():
        mas = list(map(int, input("Введіть список ваг через пробіл: ").split()))
        identlims(mas)

if __name__ == "__main__":
        test_sklad()