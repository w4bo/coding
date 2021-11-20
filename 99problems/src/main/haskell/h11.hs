data Cardinality a = Multiple Int a | Single a | Empty deriving (Show, Eq)
encodeModified :: Eq a => [a] -> [Cardinality a]
encodeModified [] = []
encodeModified l = foldr (\element acc -> g element (head acc) ++ tail acc) [Empty] l

g :: Eq a => a -> Cardinality a -> [Cardinality a]
g element (Multiple i e)
		| element == e = [Multiple (i+1) e]
		| otherwise = [Single element, Multiple i e]
g element (Single e) 
		| element == e = [Multiple 2 e]
		| otherwise = [Single element, Single e]
g element (Empty) = [Single element]

test :: Bool
test = 
	encodeModified "anna" == [Single 'a',Multiple 2 'n',Single 'a'] && 
	encodeModified "aaaabccaadeeee" == [Multiple 4 'a',Single 'b',Multiple 2 'c',Multiple 2 'a',Single 'd',Multiple 4 'e']