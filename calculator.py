#Calculator
#Diego Peña 10-I

import math

calculations = ["add", "substract", "multiply", "divide", "square root"]

while True:
            try:
                do_math = input("What calculation would you like to do? You can choose from: \n\nAdd \nSubstract \nMultiply \nDivide\nSquare Root\n\n").lower()
                
                if do_math not in calculations:
                    raise ZeroDivisionError("write the calculation you'd like as it's shown.")
                
                if do_math == "square root":
                    n1 = int(input("Enter a number: "))
                    print(math.sqrt(n1))
                    break
                              

                n1 = int(input("Enter a number: "))
                n2 = int(input("Enter another number: "))

                match do_math:
                    case "add":
                        print (n1 + n2)
                    case "substract":
                        print (n1 - n2)
                    case "multiply":
                        print (n1 * n2)
                    case "divide":
                        print (n1 / n2)
                break

            except:
                print("Please write the calculation you'd like as it's shown and follow the instructions.")
            