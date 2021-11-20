repli :: [a] -> Int -> [a]
repli _ 0 = []
repli [] n = []
repli l n = foldr (\element acc -> f element n ++ acc) [] l

f :: a -> Int -> [a]
f _ 0 = []
f element n = element : f element (n-1)

test = 
	repli "anna" 3 == "aaannnnnnaaa"