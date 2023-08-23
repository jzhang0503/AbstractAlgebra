#class with methods to check for properties of groups

import numpy as np
import math

def check_add_inverse_mod_n(lst, n: int) -> bool:
    lst = [float(element) for element in lst]
    lst2 = lst.copy()

    for element in lst:
         index = 0
         while index < len(lst2):
            if (element + lst2[index]) % n == 0:
                break
            index += 1
            if index == len(lst2):
                 return False
    
    return True

def is_group(items: str,operation: str) -> str:
    numset = items.split(',')           
    try:
        numset = [float(element) for element in numset]
    except ValueError:
        return "Error: Set contains non-numeric elements"
    
    if "add" in operation:
        operation = operation.split(" ")
        operation.remove("add")
        operation.remove("mod")
        if len(operation) > 1:
            return "Error: Incorrect operation format"
        n = float(operation[0])

        if float(0) not in numset:
                return "Error: Set does not contain identity element"
        for element in numset:
            for b in numset:
                #check closure
                if ((float(element) + float(b))% n) not in numset:
                    return "Error: Set is not closed under addition"
                #check for inverses
                if check_add_inverse_mod_n(numset, n) == False:
                    return "Error: Set does not contain inverses"

        #check for associativity
        for c in numset:
                if (float(element) + float(b)) + float(c) != float(element) + (float(b) + float(c)):
                    return "Error: Addition is not associative"
        
        return "Success: Set is a group under addition mod " + str(n)
    
    if "mult" in operation:
        operation = operation.split(" ")
        operation.remove("mult")
        operation.remove("mod")
        if len(operation) > 1:
            return "Error: Incorrect operation format"
        if 1 not in numset:
                    return "Error: Set does not contain identity element"
           
        if len(operation)== 0:
             for element in numset:
                for b in numset:
                    #check closure
                    if (float(element) * float(b)) not in numset:
                        return "Error: Set is not closed under multiplication"
                    #check for inverses
                    if (float(element) * float(b)) != 1:
                        return "Error: Set does not contain inverses"
                for c in numset:
                    if (float(element) * float(b)) * float(c) != float(element) * (float(b) * float(c)):
                        return "Error: Multiplication is not associative"    
                return "Success: Set is a group under multiplication"
             
        else:
            n = float(operation[0])

          
            for element in numset:
                for b in numset:
                    #check closure
                    if ((float(element) * float(b))% n) not in numset:
                        return "Error: Set is not closed under multiplication"
                    #check for inverses
                    if (float(element) * float(b))% n != 1:
                        return "Error: Set does not contain inverses"

            #check for associativity
            for c in numset:
                    if (float(element) * float(b)) * float(c) != float(element) * (float(b) * float(c)):
                        return "Error: Multiplication is not associative"
            
            return "Success: Set is a group under multiplication mod " + str(n)