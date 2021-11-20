myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs
-- (+10) 1 = 11
-- (+) 1 10 = 11
myLength' :: [a] -> Int
myLength' [] = 0
myLength' (x:xs) = foldr (\x -> (+) 1) 1 xs

test = 
	myLength [] == 0 &&
	myLength [1,2,3,4] == 4 &&
	myLength' [] == 0 &&
	myLength' [1,2,3,4] == 4 &&
	myLength' [4] == 1