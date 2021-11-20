encode :: Eq a => [a] -> [(Int, a)]
encode [] = []
encode l = foldr (\element acc -> 
		if acc /= [] && snd (head acc) == element then
			 (fst (head acc) + 1, element) : tail acc
		else (1, element) : acc
	) [] l

test :: Bool
test = 
	encode "anna" == [(1,'a'),(2,'n'),(1,'a')] &&
	encode "aaaaabbbbccceed" == [(5,'a'),(4,'b'),(3,'c'),(2,'e'),(1,'d')]