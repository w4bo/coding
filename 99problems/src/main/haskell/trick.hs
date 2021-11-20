fr :: [Int] -> Int
fr [] = 0
fr l = foldr (-) 1 l 
-- (2 - 1)
-- (2 - (3 - 1))
-- (2 - (3 - (4 - 1)))

fl :: [Int] -> Int
fl [] = 0
fl l = foldl (-) 1 l
-- (1 - 1)
-- ((1 - 1) - 2)
-- ((1 - 1) - 2) - 3) 

test :: Bool
test = 
	fl [1,2,3] == -5 &&
	fr [1,2,3] == 1 && 
	fl [2] == -1 &&
	fr [2] == 1


-- zip :: [a] -> [b] -> [(a, b)]
-- base Prelude, base Data.List
-- zip takes two lists and returns a list of corresponding pairs. 
-- If one input list is short, excess elements of the longer list are discarded
-- zip [0..] ys = [(0, ...), ... (n-1, ...)]

-- inserting element at an index, using foldr
insertAt :: a -> [a] -> Int -> [a]
insertAt x ys n = foldr insertHelper [] $ zip [0..] ys
    where
        insertHelper (i,y) acc = if i == n
            then x : y : acc
            else y : acc