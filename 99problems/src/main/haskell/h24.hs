import Data.List
import System.Random
rndGen :: Int -> Int -> [Int]
rndGen i m = take i $ randomRs (1, m) (mkStdGen 1)

test :: Bool
test =
  rndGen 4 3 == [3,2,2,3]

  
-- randomR :: RandomGen g => (a, a) -> g -> (a, g)
-- Takes a range (lo,hi) and a random number generator g, and returns a random 
-- value uniformly distributed in the closed interval [lo,hi], together with a 
-- new generator. It is unspecified what happens if lo>hi
-- random :: RandomGen g => g -> (a, g)
-- The same as randomR, but using a default range determined by the type:
-- 
-- For bounded types (instances of Bounded, such as Char), the range is 
-- normally the whole type.
-- For fractional types, the range is normally the semi-closed interval [0,1).
-- For Integer, the range is (arbitrarily) the range of Int.
-- randomRs :: RandomGen g => (a, a) -> g -> [a]
-- Plural variant of randomR, producing an infinite list of random values
-- instead of returning a new generator.