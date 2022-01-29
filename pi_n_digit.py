from pytest import mark
import math

@mark.pi_n_digit
def test_pi():
    res = pi_n(3)
    assert res == 3.142

def pi_n(num: int):
    '''
    Function to calculate PI to a certain number
    '''
    return round(math.pi, num)

if __name__ == "__main__":
    n = int(input("Enter number between 1 to 10: "))
    print(pi_n(n))