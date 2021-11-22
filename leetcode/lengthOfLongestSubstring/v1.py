def test_function(s: str) -> int:
    acc = [] # cur string accumulator
    m = -1 # initial counter
    for i in s: # iterate over the elements of the list
        if i not in acc: # if the char is new
            acc.append(i) # add it
        else: # else
            m = max(m, len(acc)) # update the counter
            acc = acc[acc.index(i) + 1:] # remove from the accumulator all the character until the repeated one
            acc.append(i) # add the current character
    return max(m, len(acc)) # return the maximum length
