from pytest import mark
import math

@mark.next_prime_number
def test_next_prime_number():
    res = next_prime_number(650)
    assert res, [2,5,5,13]
    res = next_prime_number(100)
    assert res, [2,2,5,5]

def next_prime_number(num: int):
    '''
    Prime Factor Function
    :param num: Number to find prime factors
    :type num: integer
    :return: List of all prime factors
    :rtype: list
    '''
    prime_factors = []
    temp = num
    if num > 2:
        while (num%2 == 0):
            num = num / 2
            prime_factors.append(2)
        for i in range(3, int(math.sqrt(num))+1, 2):
            while (num%i == 0):
                num = num / i
                prime_factors.append(int(i))
        if num != 1:
            prime_factors.append(int(num))
    else:
        return "Number Less than 2"
    return prime_factors

if __name__ == "__main__":
    while True:
        n = input("Enter a number or Type exit: ")
        if n == 'exit':
            break
        print(next_prime_number(int(n)))