import math
if __name__ == '__main__':
    cost = float(input("Enter the cost : "))
    money = float(input("Money paid : "))
    change = round(money - cost, 3)
    print("Return Change : ", change)
    change = change * 100
    quarter = math.floor(change / 25)
    change = change % 25
    dime = math.floor(change / 10)
    change = change % 10
    nickel = math.floor(change / 5)
    penny = int(change % 5)
    print("Return : \n Quarter : {} \n Dime : {} \n Nickel : {} \n Penny : {} ".format(quarter,dime,nickel, penny))
