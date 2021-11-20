my_last(H, [H]).
my_last(X, [_|T]) :- my_last(X, T).

test() :- 
	my_last(X, [1,2,3]), X == 3,
	my_last(Y, [1,2]), Y == 2.
