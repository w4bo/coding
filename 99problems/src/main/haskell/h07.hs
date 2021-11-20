data NestedList a = Elem a | List [ NestedList a ]
-- lists are homogeneous in Haskell, we need a data type
-- Elem a : is a single element
-- List [ NestedList a ] : is a list (of ˋNestedListˋs) of ˋElemˋs 

flatten :: NestedList a -> [a]
flatten (List []) = []
flatten (Elem x) = [x]
flatten (List (x:xs)) = (flatten x) ++ (flatten (List xs)) 

test :: Bool
test = flatten (Elem 1) == [1] &&
		flatten (List [Elem 1]) == [1] &&
		flatten (List [Elem 1, Elem 2, (List [Elem 3, (List [Elem 4])])]) == [1,2,3,4]
