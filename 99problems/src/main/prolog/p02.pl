my_but_last(H, [H, _]).
my_but_last(X, [_ | T]) :- my_but_last(X, T).

test() :- 
	my_but_last(X, [1,2,3]), X == 2,
	my_but_last(Y, [1,2]), Y == 1.
