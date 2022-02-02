from pytest import mark

@mark.calculator
class CalculatorTest:

    def test_sum(self):
        assert Calculator(25, 25).add() == 50

    def test_subtract(self):
        assert Calculator(25, 25).subtract() == 0

    def test_multiply(self):
        assert Calculator(25, 25).multiply() == 625

    def test_divide(self):
        assert Calculator(25, 25).divide() == 1


class Calculator:
    def __init__(self, num1, num2):
        """
        Initializing the class function
        :param num1: First number
        :type num1: int
        :param num2: Second number
        :type num2: int
        """
        self.num1 = num1
        self.num2 = num2

    def multiply(self):
        """
        Multiplication Function
        :return: Multiplied Number
        :rtype: int
        """
        return self.num1 * self.num2

    def add(self):
        """
        Addition Function
        :return: Added Number
        :rtype: int
        """
        return self.num1 + self.num2

    def subtract(self):
        """
        Subtraction Function
        :return: Subtracted Number
        :rtype: int
        """
        return self.num1 - self.num2

    def divide(self):
        """
        Divide Function
        :return: Divided by a number
        :rtype: int
        """
        return self.num1 / self.num2


if __name__ == "__main__":
    while True:
        c = input("Type operation symbol or exit: ")
        if c == 'exit':
            break
        a = int(input("Enter the number :"))
        b = int(input("Enter the number :"))
        cal = Calculator(a, b)
        if c == '*':
            ans = cal.multiply()
        if c == '+':
            ans = cal.add()
        if c == '-':
            ans = cal.subtract()
        if c == '/':
            ans = cal.divide()
        print("Answer is : ", ans)
