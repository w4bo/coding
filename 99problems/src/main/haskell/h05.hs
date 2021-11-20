myReverse :: Ord a => [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

myReverse' :: Ord a => [a] -> [a]
myReverse' [] = []
myReverse' (x:xs) = foldl (\acc element -> if (element == head acc) then acc else element:acc) [x] (xs)

test = 
	myReverse [1,2,3] == [3,2,1] &&
	myReverse [1,2] == [2,1] &&
	myReverse [1] == [1] &&
	myReverse' [1,2,3] == [3,2,1] &&
	myReverse' [1,2] == [2,1] &&
	myReverse' [1] == [1] 