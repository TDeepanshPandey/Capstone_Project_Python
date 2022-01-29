from pytest import mark
import math

@mark.e_n_digit
def test_pi():
    res = e_n(3)
    assert res == 2.718

def e_n(num: int):
    '''
    Function to calculate PI to a certain number
    '''
    return round(math.e, num)

if __name__ == "__main__":
    n = int(input("Enter number between 1 to 10: "))
    print(e_n(n))