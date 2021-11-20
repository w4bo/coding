-- Implement the so-called run-length encoding data compression method directly. 
-- I.e. don't explicitly create the sublists containing the duplicates, as in problem 9, 
-- but only count them. As in problem P11, simplify the result list by replacing the singleton 
-- lists (1 X) by X. 
-- ALREADY DONE IN h11.hs, a variation has been proposed here 

data Cardinality a = Multiple Int a | Single a | Empty deriving (Show, Eq)
encodeDirect :: Eq a => [a] -> [Cardinality a]
encodeDirect [] = []
encodeDirect (x:xs) = fst res : encodeDirect (snd res)
	where res = f x (x:xs) (Empty, [])

-- a : current element
-- [a] : overall list
-- (Cardinality a, [a]) : (cardinality of the current element, remaining list)
-- (Cardinality a, [a]) : result
f :: Eq a => a -> [a] -> (Cardinality a, [a]) -> (Cardinality a, [a])
f _ [] res = res
f element (x:xs) (Empty, [])
	| element == x = f element xs (Single element, [])
	| otherwise = f element xs (Empty, [x])
f element (x:xs) (Single _, acc)
	| element == x = f element xs (Multiple 2 element, acc)
	| otherwise = f element xs (Single element, acc ++ [x])
f element (x:xs) (Multiple i _, acc)
	| element == x = f element xs (Multiple (i+1) element, acc)
	| otherwise = f element xs (Multiple i element, acc ++ [x])

test :: Bool
test = 
	encodeDirect "aaaabccaadeeee" == [Multiple 6 'a',Single 'b',Multiple 2 'c',Single 'd',Multiple 4 'e'] &&
	encodeDirect "anna" == [Multiple 2 'a',Multiple 2 'n']