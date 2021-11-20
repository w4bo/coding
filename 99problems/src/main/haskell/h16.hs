dropEvery :: [a] -> Int -> [a]
dropEvery [] _ = []
dropEvery _ 0 = []
dropEvery _ 1 = []
dropEvery l n = foldl (\acc (index, element) -> 
		if index `mod` n == 0 then 
			acc 
		else acc ++ [element]
	) [] $ zip [1..] l

test :: Bool
test =
	dropEvery "anna" 2 == "an" &&
	dropEvery "The quick brown fox jumps over the lazy dog" 4 == "Thequik bownfoxjums oer he azydog"