removeAt :: [a] -> Int -> [a]
removeAt [] _ = []
removeAt l i = foldr (\(element, index) acc -> if index == i then acc else element:acc) [] $ zip l [1..]

-- this solution do not need to iterate over all the elements of the list
removeAt' :: [a] -> Int -> [a]
removeAt' [] _ = []
removeAt' (x:xs) 1 = xs
removeAt' (x:xs) i = x : removeAt' xs (i-1)

test :: Bool
test =
  removeAt "anna" 1 == "nna" &&
  removeAt "anna" 5 == "anna" &&
  removeAt "anna" 0 == "anna" &&
  removeAt' "anna" 1 == "nna" &&
  removeAt' "anna" 5 == "anna" &&
  removeAt' "anna" 0 == "anna"
