import Data.List.Split
import System.Environment

--Funció per llegir un fitxer
readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile


--Funció que donada una llista dona llista de llistes en la que en la primera posició te tota la llista
-- i en les següents contenen la llista menys el primer element
fragmentList:: [([Char], Int)] -> [[([Char], Int)]]
fragmentList [] = []
fragmentList xs = xs : fragmentList (tail xs)


--Funció que donada una tupla de ([Char], Int) i una llista dels mateixos elements, la busque i la elimine
remove :: [([Char], Int)] -> ([Char], Int) -> [([Char], Int)]
remove [] y = []
remove (x:xs) y
  | x == y = remove xs y
  | otherwise = x : remove xs y


--Conjunt de funcions que retorna una llista de llistes amb les diferents seqüencies ascendents que ha trobat
findSequence :: [[([Char], Int)]] -> [[([Char], Int)]]
findSequence []                 = []
findSequence (x:xs)             = (findSequence' (tail x) ("head x", 0) (tail x)) : findSequence xs

findSequence' :: [([Char], Int)] -> ([Char], Int) -> [([Char], Int)] -> [([Char], Int)]
findSequence' [] y z = z
findSequence' (x:xs) y z
  | (snd x) <= (snd y) = findSequence' (remove z x) ("head x", 0) (remove z x)
  | otherwise = findSequence' xs x z


--Conjunt de funcions que retorna una llista amb ls seqüència més llarga trobada
findLongestList :: [[([Char], Int)]] -> [([Char], Int)]
findLongestList (x:[]) = x
findLongestList (x:xs) = findLongestList' xs x

findLongestList' :: [[([Char], Int)]] -> [([Char], Int)] -> [([Char], Int)]
findLongestList' (x:[]) y = y
findLongestList' (x:xs) y
  | length x > length y = findLongestList' xs x
  | otherwise = findLongestList' xs y


main = do
    args <- getArgs
    content <- readFile (head args)
    let splitlist = splitOn "\n" content
    let splitlist' = [splitOn " " x | x <- splitlist]
    let l = init splitlist'
    let theList = [(x!!0, read (x!!1) :: Int) | x <- l]
    let fragments = fragmentList theList
    let sequences = findSequence fragments
    let seq = findLongestList sequences
    let res = [(fst ele) ++ " " ++ (show (snd ele)) | ele <- seq]
    mapM_ putStrLn res
