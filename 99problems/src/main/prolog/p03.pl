element_at(H, [H|_], 1).
element_at(X, [_|T], N) :- 
	M is N - 1, 
	element_at(X, T, M).

test() :- 
	element_at(X, [4,2,3], 1), X == 4,
	element_at(Y, [1,2], 2), Y == 2.