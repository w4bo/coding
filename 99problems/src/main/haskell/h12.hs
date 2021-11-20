data Cardinality a = Multiple Int a | Single a | Empty deriving (Show, Eq)

decodeModified :: [Cardinality a] -> [a]
decodeModified = foldr (\element acc -> d element ++ acc) []

d :: Cardinality a -> [a]
d Empty = []
d (Single e) = [e]
d (Multiple 0 e) = []
d (Multiple i e) = e : d (Multiple (i-1) e)

test :: Bool
test =
	decodeModified [Single 'a',Multiple 2 'n',Single 'a'] == "anna" && 
	decodeModified [Multiple 4 'a',Single 'b',Multiple 2 'c',Multiple 2 'a',Single 'd',Multiple 4 'e'] == "aaaabccaadeeee"