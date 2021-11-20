dupli :: [a] -> [a]
dupli [] = []
dupli l = foldr (\elem acc -> [elem, elem] ++ acc) [] l

test :: Bool
test = 
	dupli "anna" == "aannnnaa"