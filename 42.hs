import System.IO
import Data.Char

main = do
    handle <- openFile "42_words.txt" ReadMode
    contents <- hGetContents handle
    print $ sum [1 | x <- words contents, isTriangleWord x]

triangle_numbers = map (\x -> x*(x+1) `quot` 2) [1..]
isTriangleNumber::Int -> Bool
isTriangleNumber x =
    temp x triangle_numbers
    where
        temp y (z:zs)
            | y == z = True
            | y < z = False
            | otherwise = temp y zs

isTriangleWord x = isTriangleNumber . sum $ map (\x -> ord x - 64) x
