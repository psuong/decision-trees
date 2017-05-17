from pasta import Pasta

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