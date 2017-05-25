class Pasta(object):
    def __init__(self, name, sauce_color, has_meat, has_seafood, like):
        self.data = {
            "name": name,
            "sauce_color": sauce_color,
            "has_meat": has_meat,
            "has_seafood": has_seafood,
            "like": like
        }
    def __str__(self):
        return self.data["name"]


def split_data(attribute: str, data: []) -> {}:
    """
    Returns a tuple of partitioned data given the key
    """
    partitioned_data = {}

    for element in data:
        attribute_value = element.data[attribute]
        if attribute_value not in partitioned_data:
            partitioned_data[attribute_value] = [element]
        else:
            partitioned_data[attribute_value].append(element)
    return partitioned_data
