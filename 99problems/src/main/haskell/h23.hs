import Data.List
import System.Random
rndSelect :: [a] -> Int -> [a]
rndSelect _ 0 = []
rndSelect l n = foldr (\i acc -> l !! i : acc) [] indexes
  where indexes = take n $ randomRs (0, (length l)-1) (mkStdGen 1)

test :: Bool
test =
  rndSelect "abcdefghilmnopqrstuvz" 1 == "c" &&
  rndSelect "abcdefghilmnopqrstuvz" 2 == "cv" &&
  rndSelect "abcdefghilmnopqrstuvz" 4 == "cvpt"
