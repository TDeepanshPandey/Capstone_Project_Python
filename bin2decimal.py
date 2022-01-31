def bin2decimal(number: str):
    """
    Function to convert binary to decimal
    :param number: A decimal number
    :type number: integer
    :return: Binary value
    :rtype: integer
    """
    answer = 0
    for d in number:
        answer = answer * 2 + int(d)
    return answer


def dec2binary(number: int, ans_pr: list):
    """
    Function to convert decimal to binary
    :param number: A number
    :type number: integer
    :param ans_pr: A list to story 1 or 0 value
    :type ans_pr: list
    :return: list of 1 and 0 values
    :rtype: list
    """
    if number >= 1:
        dec2binary(number // 2, ans_pr)
    ans_pr.append(number % 2)


if __name__ == "__main__":
    option = int(input("Choose \n 1. Decimal to Binary \n 2. Binary to Decimal \n"))
    if option == 1:
        num = int(input("Enter a decimal value : "))
        ans = []
        dec2binary(num, ans)
        print("Binary Value is ",''.join([str(i) for i in ans]).lstrip('0'), "\n", end='')
    if option == 2:
        num = input(" Enter a binary value : ")
        print("Decimal Value is ", bin2decimal(num))