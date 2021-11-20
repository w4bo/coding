insertAt :: [a] -> a -> Int -> [a]
-- it does not work if i == 0 or i > length list
insertAt l x i = foldr (\(element, idx) acc -> if idx == i then [x, element] ++ acc else element:acc) [] $ zip l [1..]

insertAt' :: [a] -> a -> Int -> [a]
insertAt' [] x _ = [x]
insertAt' (y:ys) x 0 = [x, y] ++ ys
insertAt' (y:ys) x 1 = [x, y] ++ ys
insertAt' (y:ys) x i = y : insertAt' ys x (i-1)

test :: Bool
test =
  insertAt' "anna" 'b' 0 == "banna" &&
  insertAt' "anna" 'b' 1 == "banna" &&
  insertAt' "anna" 'b' 4 == "annba" &&
  insertAt' "anna" 'b' 5 == "annab" &&
  insertAt' "anna" 'b' 2 == "abnna"
