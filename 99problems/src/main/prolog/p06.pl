myReverse(X, [H|T], R) :- myReverse(X, T, [H|R]).
myReverse(R, [], R).

isPal(X, [H|T1], [H|T2]) :- isPal(X, T1, T2).
isPal(true, [], []).
isPal(false, _, _).

isPalindrome(X, L) :- myReverse(Y, L, []), isPal(X, L, Y).

test() :- 
	isPalindrome(X, [1,2,3]), X == false,
	isPalindrome(Y, []), Y == true,
	isPalindrome(Z, [1,2,3,2,1]), Z == true.

