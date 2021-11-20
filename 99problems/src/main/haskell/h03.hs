elementAt :: [a] -> Int -> a
elementAt [] _ = error "not found" 
elementAt (x:xs) i = 
	if i == 1 then x 
	else elementAt xs (i-1)

elementAt' [] _ = error "not found" 
elementAt' (x:_) 1 = x 
elementAt' (_:xs) i = elementAt' xs (i-1)

test = 
	elementAt [1,2,3] 1 == 1 &&
	elementAt [1,2,3] 2 == 2 &&
	elementAt [1,2,3] 3 == 3 &&
	elementAt' [1,2,3] 1 == 1 &&
	elementAt' [1,2,3] 2 == 2 &&
	elementAt' [1,2,3] 3 == 3 