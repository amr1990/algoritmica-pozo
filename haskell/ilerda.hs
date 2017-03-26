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

--Conjunt de funcions que retorna una llista de llistes amb les diferents seqüencies ascendents que ha trobat
findSequences :: [[([Char], Int)]] -> [[([Char], Int)]]
findSequences []                 = []
findSequences (x:zs) = findSequence x : (findSequences zs)

findSequence :: [([Char], Int)] -> [([Char], Int)]
findSequence []   = []
findSequence (x:xs) = x : findSequence' xs x

findSequence' :: [([Char], Int)] -> ([Char], Int) -> [([Char], Int)]
findSequence' [] y                     = []
findSequence' (x:zs) y
  | (snd x) < (snd y) = findSequence' zs y
  | (snd x) > (snd y) = x : findSequence' zs x
  | length(zs) == 0 && (snd x) > (snd y) = x : findSequence' zs x
  | otherwise = findSequence' zs y


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
    let sequences = findSequences fragments
    let seq = findLongestList sequences
    let res = [(fst ele) ++ " " ++ (show (snd ele)) | ele <- seq]
    mapM_ putStrLn res
