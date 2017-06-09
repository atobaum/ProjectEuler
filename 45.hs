main = do
    print $ take 3 allOfThree

triangle_numbers = map (\x -> x*(x+1) `quot` 2) [1..]
pentagonal_numbers = map (\x -> x*(3*x-1) `quot` 2) [1..]
hexagonal_numbers = map (\x -> x*(2*x-1)) [1..]

allOfThree = filter (\x -> isInSortedList x triangle_numbers) $ filter (\x -> isInSortedList x pentagonal_numbers) hexagonal_numbers

isInSortedList::(Ord a) => a -> [a] -> Bool
isInSortedList x (y:ys)
    | x == y = True
    | x < y = False
    | otherwise = isInSortedList x ys
