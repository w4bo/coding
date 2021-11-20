compress :: Eq a => [a] -> [a]
compress [] = []
compress (x:xs) = reverse (foldl (\acc element -> if element == head acc then acc else element:acc) [x] xs)

compress' :: Eq a => [a] -> [a]
compress' [] = []
compress' (x:xs) = foldr (\element acc -> if acc /= [] && element == head acc then acc else element:acc) [] (x:xs)

test :: Bool
test = 
	compress "anna" == "ana" &&
	compress "ana" == "ana" &&
	compress' "anna" == "ana" &&
	compress' "ana" == "ana"