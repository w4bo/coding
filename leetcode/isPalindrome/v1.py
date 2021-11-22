def test_function(x: int) -> bool:
    x = str(x) # conver the number to string
    for i in range(int(len(x) / 2)): # iterate for half the string
        if not x[i] == x[-i - 1]: # check if the digit are the same
            return False # if not return false
    return True # if here, return true