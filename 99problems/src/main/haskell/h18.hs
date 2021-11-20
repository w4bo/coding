slice :: [a] -> Int -> Int -> [a]
slice [] _ _ = []
slice l from to = foldr (\(element, index) acc ->
    if index < from || index > to then
      acc
    else
      element : acc
  ) [] $ zip l [1..]

test :: Bool
test =
  slice "abcdefghilmno" 1 13 == "abcdefghilmno" &&
  slice "abcdefghilmno" 2 4 == "bcd" &&
  null (slice "" 1 2)
