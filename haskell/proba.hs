import Data.List.Split

readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile


remove :: (Ord a)=>[a] -> a -> [a]
remove [] _ = []
remove (x:xs) y
 | x > y     = remove xs y
 | otherwise = x : remove xs y

sumEveryTwo :: [Int] -> Int ->[Int]
sumEveryTwo [] 0          = []     -- Do nothing to the empty list
sumEveryTwo (x:[]) 0      = [x]    -- Do nothing to lists with a single element
sumEveryTwo [] z          = []
sumEveryTwo (x:(y:zs)) z
 | y > x && x > z = x : y : sumEveryTwo zs y
 | y > z    = y : sumEveryTwo zs y
 | x > y    = x : sumEveryTwo zs x
 | otherwise = sumEveryTwo zs z


main = do
  content <- readLines "cargament.txt"
  let intlist = [(splitOn " " item) | item <- content]
  --let li = [[obj!!0, ob!!1] | obj <- intlist]
  let a = sumEveryTwo [1,3,2,5,1,2,3,4] 0
  print intlist
  print a
  --print li
