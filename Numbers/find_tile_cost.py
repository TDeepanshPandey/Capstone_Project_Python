from pytest import mark


@mark.find_tile_cost
def test_find_tile_cost():
    """
    Function to test total cost
    :return: Total Cost
    :rtype: integer
    """
    assert find_tile_cost(10, 10, 2), 200


def find_tile_cost(width: int, height: int, cost: int):
    """
    Finding the total cost for given parameters
    :param width: Width of Floor plan
    :type width: integer
    :param height: Height of Floor plan
    :type height: integer
    :param cost: Cost of Floor plan
    :type cost:  integer
    :return: Total cost
    :rtype: integer
    """
    return round(width * height * cost, 2)


if __name__ == "__main__":
    w = int(input("Enter Width : "))
    h = int(input("Enter Height: "))
    c = int(input("Enter Tile Cost : "))
    print("Total Cost : ", find_tile_cost(w, h, c))
