range :: Int -> Int -> [Int]
range from to
  | from <= to = from : range (from + 1) to
  | otherwise = []

test :: Bool
test =
  range 1 10 == [1,2,3,4,5,6,7,8,9,10] &&
  null(range 2 1)
