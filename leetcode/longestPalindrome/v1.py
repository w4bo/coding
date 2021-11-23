def test_function(orig: str) -> str:
    best = ""  # best palindrome string
    acc = ""  # current palindrome accumulator
    for i in range(len(orig)):  # iterate over the elements of the list
        s = orig  # restore the string
        acc = s[i]  # initialize the accumulator
        first = True  # use this flag to try the addition of the special character "?" only once
        j = 0
        # iterate to check the characters surrounding c[i]
        while j < len(s) / 2:
            j += 1  # increase the counter
            if i - j >= 0 and i + j <= len(s):
                if i + j < len(s) and s[i - j] == s[i + j]:  # check if the two surrounding characters are the same
                    # if so, concatenate the string
                    acc = s[i - j] + acc + s[i + j]
                elif first:  # else, since this might be the case of a palindrome string with an even number of characters
                    best = best if len(best) >= len(acc) else acc  # update the be
                    first = False
                    acc = "?"
                    # add to the string the special character
                    s = s[:i] + acc + s[i:]
                    j = 0  # and retry if the string is palindrom
                else:
                    break
            else:
                break
        acc = acc.replace("?", "")  # replace the special character, if any
        best = best if len(best) >= len(acc) else acc  # update the best
    return best  # return the maximum string
