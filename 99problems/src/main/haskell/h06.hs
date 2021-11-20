isPalindrome:: Eq a => [a] -> Bool
isPalindrome [] = True 
isPalindrome [_] = True 
isPalindrome l = isPal l (reverse l) (length l `quot`2)  
-- there is no need to check the 'pivot'

isPal:: Eq a => [a] -> [a] -> Int -> Bool
isPal l1 l2 0 = True
isPal (x:xs) (y:ys) l
	| x == y = isPal xs ys (l-1)
	| otherwise = False

---------------------------------------------------------
-- 'Less efficient' solution ----------------------------
-- There is no need to check the entire list but the half
-- Actually, I am adding two function calls "trunc l" and
-- "trunc reverse l".
---------------------------------------------------------
trunc:: [a] -> [a]
trunc [] = []
trunc l = trunc' l size
	where 
		s = length l 
		size = s `quot` 2 
			-- there is no need to check the 'pivot'
			--if (s)%2 == 1 
			--	then (s + 1)/2 
			--	else s/2

trunc' (x:xs) 0 = []
trunc' (x:xs) l = x : trunc' xs (l-1)

isPalindrome':: Eq a => [a] -> Bool
isPalindrome' [] = True 
isPalindrome' [_] = True 
isPalindrome' l = isPal' (trunc l) (trunc (reverse l)) 

isPal':: Eq a => [a] -> [a] -> Bool
isPal' [] [] = True
isPal' (x:xs) (y:ys)
	| x == y = isPal' xs ys
	| otherwise = False

test =
	isPalindrome [1,2,1] && 
	isPalindrome "anna" && 
	not (isPalindrome "ann") &&
	isPalindrome' [1,2,1] && 
	isPalindrome' "anna" && 
	not (isPalindrome' "ann")