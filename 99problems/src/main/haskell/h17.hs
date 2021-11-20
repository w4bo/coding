split :: [a] -> Int -> ([a], [a])
split [x] i = ([x], [])
split (x:xs) 0 = ([], x:xs)
split (x:xs) i = (x : fst res, snd res)
  where res = split xs (i-1)

test :: Bool
test =
  split "anna" 1 == ("a", "nna") &&
  split "anna" 5 == ("anna", []) &&
  split "anna" 0 == ([], "anna")
