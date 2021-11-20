myLast :: [a] -> a
myLast [] = error "empty list"
myLast [x] = x
myLast (_:xs) = myLast xs  


myLast' :: [a] -> a
myLast' [] = error "empty list"
myLast' (x:xs) = foldr (\x y -> y) x xs
