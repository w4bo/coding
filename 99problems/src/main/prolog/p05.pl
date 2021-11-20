my_reverse(X, L) :- my_rev(X, L, []).
my_rev(R, [], R).
my_rev(X, [H|T], R) :- my_rev(X, T, [H|R]).

test() :-
	my_reverse(X, [1,2,3,4]), X == [4,3,2,1],
	my_reverse(Y, []), Y == [].