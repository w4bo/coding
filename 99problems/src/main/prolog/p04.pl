my_len(H, [], H).
my_len(X, [_|T], Y) :- Z is Y + 1, my_len(X, T, Z).
my_length(X, Y) :- my_len(X, Y, 0).

test() :-
	my_length(X, []), X == 0,
	my_length(Y, [1,2,3,4]), Y == 4.