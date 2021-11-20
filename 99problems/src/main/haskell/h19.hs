rotate :: [a] -> Int -> [a]
rotate [] _ = []
rotate l i = if i >= 0 then res else reverse res
  where
    acc = if i < 0 then r (reverse l) (abs i) else r l i
    res = snd acc ++ fst acc

r :: [a] -> Int -> ([a], [a])
r [] _ = ([], [])
r (x:xs) 0 = ([], x:xs)
r (x:xs) i = (x : fst res, snd res)
  where res = r xs (i-1)
  
test :: Bool
test =
  rotate "abcdefgh" 3 == "defghabc" &&
  rotate "abcdefgh" (-2) == "ghabcdef"
