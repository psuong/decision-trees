from pasta import Pasta, split_data
import math


def calc_entropy(p_pos, p_neg):
    if p_pos == 0:
        return -p_neg * math.log(p_neg, 2)
    elif p_neg == 0:
        return -p_pos * math.log(p_pos, 2)
    else:
        return -p_pos * math.log(p_pos, 2) - p_neg * math.log(p_neg, 2) 


def calc_entropy_bool_data(data: []):
    p_pos = sum(data) / len(data)
    p_neg = 1 - p_pos
    return calc_entropy(p_pos, p_neg)


def calc_entropy_pasta_data(data: []):
    """
    Takes in an array of Pasta objects.
    """
    bool_array = [pasta.data["like"] for pasta in data]
    return calc_entropy_bool_data(bool_array)


def calc_info_gain(attribute_dict: {}):
    total_bool_arr = []
    for key, value in attribute_dict.items():
        bool_array = [pasta.data["like"] for pasta in value]
        total_bool_arr.extend(bool_array)
    total_num = len(total_bool_arr)
    total_entropy = calc_entropy_bool_data(total_bool_arr)

    weighted_entropy_sum = 0
    for key, value in attribute_dict.items():
        sub_tree_entropy = calc_entropy_pasta_data(value)
        weighted_entropy_sum += sub_tree_entropy * (len(value) / total_num)
    return total_entropy - weighted_entropy_sum


def id3_pasta(data: [], attributes: [], depth: int) -> None:
    padding = depth * "\t"

    if len(attributes) == 0:
        print(padding, "Cannot determine")
        return
    best_attribute = attributes[0]
    best_attribute_data = split_data(best_attribute, data)
    best_info_gain = calc_info_gain(best_attribute_data)

    for attribute in attributes[1:]:
        partioned_data = split_data(attribute, data)
        info_gain = calc_info_gain(partioned_data)

        if info_gain > best_info_gain:
            best_attribute = attribute
            best_attribute_data = partioned_data
            best_info_gain = info_gain
    
    print("{}Best Attr: {}".format(padding, best_attribute))
    for key, value in best_attribute_data.items():
        attribute_value = "{}Attribute Value: {}".format(padding, key)
        if math.isclose(calc_entropy_pasta_data(value), 0):
            attribute_value += " -> {}".format("Like" if value[0].data["like"] else "Dislike")
            print(attribute_value)
            continue
        print(attribute_value)
        id3_pasta(value, [x for x in attributes if x != best_attribute], depth+1)


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
    attributes = ["sauce_color", "has_meat", "has_seafood"]

    # Question 1
    print("\nQuestion 1")
    id3_pasta(data, attributes, 0)

    # Question 2
    print("\nQuestion 2")
    id3_pasta(data + [extended_data[0]], attributes, 0)

    # Question 3
    print("\nQuestion 3 A")
    id3_pasta(data + [extended_data[1]], attributes, 0)
    print("\nQuestion 3 B")
    id3_pasta(data + extended_data, attributes, 0)


if __name__ == "__main__":
    main()
