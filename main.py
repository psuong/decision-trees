from pasta import Pasta
import math


def calc_entropy(p_pos, p_neg):
    if p_pos == 0:
        return -p_neg * math.log(p_neg, 2)
    elif p_neg == 0:
        return -p_pos * math.log(p_pos, 2)
    else:
        return -p_pos * math.log(p_pos, 2) - p_neg * math.log(p_neg, 2) 


def calc_entropy_data(data: []):
    p_pos = sum(data) / len(data)
    p_neg = 1 - p_pos
    return calc_entropy(p_pos, p_neg)


def main():
    data = [
        Pasta("Spaghetti with Meatballs", "red", True, False, True),
        Pasta("Spaghetti Arrabbita", "red", False, False, False),
        Pasta("Linguini Vongole", "red", False, True, False),
        Pasta("Linguini Vongole", "white", False, True, False),
        Pasta("Rigatoni alla Vodka", "pink", False, False, True),
        Pasta("Lasagne", "red", True, False, True),
        Pasta("Rigatoni Lucia", "white", False, False, True),
        Pasta("Fettucine Alfredo", "white", False, False, True),
        Pasta("Fusilli Boscaiola", "red", False, False, False),
        Pasta("Ravioli Florentine", "pink", False, False, True)
    ]
    # For future reference
    extended_data = [
        Pasta("Penne with Bolognese", "red", True, False, False),
        Pasta("Spaghetti curbonara", "white", True, False, False)
    ]


if __name__ == "__main__":
    main()
