# 99 (programming) problems

This repo collects 99 problems resolved in Haskell (functional paradigm), Prolog (logic paradigm) and Scala (multi-paradigm). The problems are gathered from the following websites:

* http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/
* http://aperiodic.net/phil/scala/s-99/
* https://wiki.haskell.org/H-99:_Ninety-Nine_Haskell_Problems

## Test
The correctness of every solution is verifiable through the invocation of test function

## Rules
*Built in features will be exploited once that they have been achieved*

## Setup of the environments

### Haskell

* sudo apt-get install haskell-platform hlint
* ghci p__.hs

### Scala

* scala
* :load /path/to/file/P__.scala
* P__.method(params)


### Prolog

* http://www.swi-prolog.org/build/Debian.html
* swipl
* consult('p__.pl')

## Problems

* P01 (*) Find the last element of a list.
    
        Example:
        ?- my_last(X,[a,b,c,d]).
        X = d

* P02 (*) Find the last but one element of a list.


* P03 (*) Find the K'th element of a list.
    The first element in the list is number 1.
    
        Example:
        ?- element_at(X,[a,b,c,d,e],3).
        X = c

* P04 (*) Find the number of elements of a list.

* P05 (*) Reverse a list.

* P06 (*) Find out whether a list is a palindrome.
    A palindrome can be read forward or backward; e.g. [x,a,m,a,x].

* P07 (**) Flatten a nested list structure.
    Transform a list, possibly holding lists as elements into a `flat' list by replacing each list with its elements (recursively).

        Example:
        ?- my_flatten([a, [b, [c, d], e]], X).
        X = [a, b, c, d, e]

    Hint: Use the predefined predicates is_list/1 and append/3

* P08 (**) Eliminate consecutive duplicates of list elements.
    If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

        Example:
        ?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
        X = [a,b,c,a,d,e]

* P09 (**) Pack consecutive duplicates of list elements into sublists.
    If a list contains repeated elements they should be placed in separate sublists.

        Example:
        ?- pack([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
        X = [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]

* P10 (*) Run-length encoding of a list.
    Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as terms [N,E] where N is the number of duplicates of the element E.

        Example:
        ?- encode([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
        X = [[4,a],[1,b],[2,c],[2,a],[1,d][4,e]]

* P11 (*) Modified run-length encoding.
    Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

        Example:
        ?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
        X = [[4,a],b,[2,c],[2,a],d,[4,e]]

* P12 (**) Decode a run-length encoded list.
    Given a run-length code list generated as specified in problem P11. Construct its uncompressed version.

* P13 (**) Run-length encoding of a list (direct solution).
    Implement the so-called run-length encoding data compression method directly. I.e. don't explicitly create the sublists containing the duplicates, as in problem P09, but only count them. As in problem P11, simplify the result list by replacing the singleton terms [1,X] by X.

        Example:
        ?- encode_direct([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
        X = [[4,a],b,[2,c],[2,a],d,[4,e]]

* P14 (*) Duplicate the elements of a list.
    
        Example:
        ?- dupli([a,b,c,c,d],X).
        X = [a,a,b,b,c,c,c,c,d,d]
