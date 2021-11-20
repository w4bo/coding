-- recursion & pattern matching
myButLast :: (Eq a) => [a] -> a
myButLast [] = error "empty list"
myButLast [_] = error "only 1 item provided"
myButLast (x:xs) = myf x xs

myf :: a -> [a] -> a
myf x [_] = x
myf y (x:xs) = myf x xs

-- pattern matching
myButLast2 :: [a] -> a
myButLast2 [x,_] = x
myButLast2 (x:xs) = myButLast2 xs

test = 
    myButLast [1,2] == 1 &&
    myButLast [1,2,3] == 2 &&
    myButLast2 [1,2] == 1 &&
    myButLast2 [1,2,3] == 2 

