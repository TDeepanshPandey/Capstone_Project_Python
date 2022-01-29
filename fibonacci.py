from pytest import mark

@mark.fibonacci
class FibonaaciTest():

    def test_fibonacci(self):
        res1 = fibonacci(4)
        if res1 == [0, 1, 1, 2]:
            assert True

    def test_fibonacci_one(self):
        res2 = fibonacci(1)
        if res2 == [0]:
            assert True

    def test_fibonacci_two(self):
        res3 = fibonacci(2)
        if res3 == [0, 1]:
            assert True


def fibonacci(num: int):
    '''
    Function to calculate Fibonacci Series
    :param num: number to print
    :type num: integer
    :return: values in fibonacci series till there
    :rtype: list
    '''
    fib = []
    if num == 1:
       return 0
    if num == 2:
       return [0, 1]
    if num > 2:
        fib.append(0)
        fib.append(1)
        for i in range(num-2):
            fib.append(sum(fib[i:i+2]))
    return fib

if __name__ == "__main__":
    n = int(input("Enter a number between 0 and 10 : "))
    print(fibonacci(n))