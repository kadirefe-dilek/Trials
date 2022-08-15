# Calculator script by Kadir Efe Dilek created on September 10, 2021 

# Main funtion to take inputs, call functions and print out messages and results.  
def main():
    print("Welcome to my calculator\n")
    
    ## Listing the commands ##
    print("""Operations:
    + -> sum
    - -> subtract
    * -> multiply
    / -> divide
    ^ -> nth power
    r -> nth root
    log -> logarithm base a
    ln -> natural logarithm
    = -> end\n
    """) # end of printing

    ## Taking first inputs ##
    number = float(input("Enter a number: "))
    oprt = input("Enter the operation: ")
    
    ## Creating a loop to take infinite inputs and calculate ##
    while(oprt != "="):
        num2 = float(input("Enter another number: "))
        if (oprt == "+"):
            number = summate(number, num2)
   
        if (oprt == "-"):
            number = subtract(number, num2)

        if (oprt == "*"):
            number = multiply(number, num2)
        
        if (oprt == "/"):
            number = divide(number, num2)

        if (oprt == "^"):
            number = takePow(number, num2)
        
        if (oprt == "r"):
            number = takeRoot(number, num2)

        if (oprt == "log"):
            number = loga(number, num2)
        
        if (oprt == "ln"):
            number = loge(number, num2)

        ## Printing a result and taking the next operation ##
        print(number)
        oprt = input("Enter the operation: ")
    # end of while loop

# end of main function


## Functions definitions to do the job ##
def summate(n1, n2):
    summation = n1 + n2
    return summation

def subtract(n1, n2):
    subtraction = n1 - n2
    return subtraction

def multiply(n1, n2):
    multiplication = n1 * n2
    return multiplication

def divide(n1, n2):
    division = n1 / n2
    return division

def takePow(n1, n2):
    power = n1 ** n2
    return power

def takeRoot(n1, n2):
    root = n1 ** (1/n2)
    return root

def loga(n1, n2):
    return

def loge(n1):
    return
# end of function definitions

    
if __name__ == "__main__":
    main()

