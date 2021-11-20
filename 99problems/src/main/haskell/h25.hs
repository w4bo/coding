import Data.List
rnd-select :: [a] -> [a]
rnd-select [] = []
rnd-select l = head permutations l