#class with methods to check for properties of groups

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

def str_to_set(items: str) -> list:
    numset = items.split(',')           
    try:
        numset = [float(element) for element in numset]
    except ValueError:
        return "Error: Set contains non-numeric elements"
    return numset

def is_group(items: str,operation: str):
    numset = str_to_set(items)
    
    if "add" in operation:
        operation = operation.split(" ")
        operation.remove("add")
        operation.remove("mod")
        if len(operation) > 1:
            return "Error: Incorrect operation format", False
        n = float(operation[0])

        if float(0) not in numset:
                return "Error: Set does not contain identity element", False
        for element in numset:
            for b in numset:
                #check closure
                if ((float(element) + float(b))% n) not in numset:
                    return "Error: Set is not closed under addition", False
                #check for inverses
                if check_add_inverse_mod_n(numset, n) == False:
                    return "Error: Set does not contain inverses", False

        #check for associativity
        for c in numset:
                if (float(element) + float(b)) + float(c) != float(element) + (float(b) + float(c)):
                    return "Error: Addition is not associative", False
        
        return ("Success: Set is a group under addition mod " + str(n)), True
    
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
                        return "Error: Set is not closed under multiplication", False
                    #check for inverses
                    if (float(element) * float(b)) != 1:
                        return "Error: Set does not contain inverses", False
                for c in numset:
                    if (float(element) * float(b)) * float(c) != float(element) * (float(b) * float(c)):
                        return "Error: Multiplication is not associative"   , False 
                return "Success: Set is a group under multiplication", True
             
        else:
            n = float(operation[0])

          
            for element in numset:
                for b in numset:
                    #check closure
                    if ((float(element) * float(b))% n) not in numset:
                        return "Error: Set is not closed under multiplication" , False
                    #check for inverses
                    if (float(element) * float(b))% n != 1:
                        return "Error: Set does not contain inverses", False

            #check for associativity
            for c in numset:
                    if (float(element) * float(b)) * float(c) != float(element) * (float(b) * float(c)):
                        return "Error: Multiplication is not associative", False
            
            return ("Success: Set is a group under multiplication mod " + str(n)), True
        

def is_sub_group(items:str, subset:str, operation:str) -> bool:
    subset = str_to_set(subset)
    numset = str_to_set(items)
    if subset == numset:
        return True, "Success: Subset is the same as the group"
    if is_group(items, operation) == False:
        return False, "Error: Set is not a group"
    for i in subset:
        if i not in numset:
            return False, "Error: Subset is not a subset of the group"
    
    for a in subset:
         for b in subset:
            if "add" in operation:
                operation = operation.split(" ")
                operation.remove("add")
                operation.remove("mod")
                if len(operation) > 1:
                    return False, "Error: Incorrect operation format"
                n = float(operation[0])
                b_inverse = (n - b) % n
                if (a + b_inverse) not in subset:
                    return False, "Error: Subset is not a subgroup by One-Step Subgroup Test"
                else:
                    return True, "Success: Subset is a subgroup by One-Step Subgroup Test"
                
def order_of_element(elt:str, items:str, operation:str) -> int:
    element = float(elt)
    numset = str_to_set(items)
    if is_group(items, operation) == False:
        return "Error: Set is not a group"
    if element not in numset:
        return "Error: Element is not in the group"
    if "add" in operation:
        operation = operation.split(" ")
        operation.remove("add")
        operation.remove("mod")
        if len(operation) > 1:
            return "Error: Incorrect operation format", False
        n = float(operation[0])
        order = 0
        while element % n != 0:
            element += element
            order += 1
    return order