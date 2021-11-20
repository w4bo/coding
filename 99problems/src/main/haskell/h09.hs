pack :: Eq a => [a] -> [[a]]
pack [] = []
pack l = packSubsequences l

packSubsequences :: Eq a => [a] -> [[a]]
packSubsequences [] = []
packSubsequences (x:xs) = [fst res] ++ packSubsequences (snd res)
	where res = packSubsequence x (x:xs)

packSubsequence :: Eq a => a -> [a] -> ([a], [a])
packSubsequence _ [] = ([], [])
packSubsequence pattern (x:xs)
	| pattern == x = (pattern : fst res, snd res)
	| otherwise = ([], x:xs)
	where res = packSubsequence pattern xs

test :: Bool
test = 
	packSubsequence 1 [1,1,2,2] == ([1,1], [2,2]) &&
	packSubsequence 1 [1] == ([1], []) &&
	pack "anna" == [['a'],['n', 'n'], ['a']] &&
	pack [1,1,2,2] == [[1, 1], [2, 2]] 