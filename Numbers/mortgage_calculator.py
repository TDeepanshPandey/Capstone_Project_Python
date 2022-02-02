if __name__ == "__main__":
    loanAmount = input('Enter loan amount \n')
    loanAmount = float(loanAmount)
    years = input('How many years will you have the loan? \n')
    years = float(years) * 12
    interestRate = input('Enter Interest Rate \n')
    interestRate = float(interestRate) / 100 / 12
    mortgagePayment = loanAmount * (interestRate * (1 + interestRate) ** years) / ((1 + interestRate) ** years - 1)
    # Prints monthly payment on next line and reformat the string to a float using 2 decimal places
    print("The monthly mortgage payment is\n (%.2f) " % mortgagePayment)
