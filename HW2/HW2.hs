module HW2
     where

-- 1
{- (a) merge2 5%-}
merge2 :: [a] -> [a] -> [a]                                                                                             -- list + list = list
merge2 [] [] = []                                                                                                       -- empty list + empty list = empty list
merge2 xs [] = xs                                                                                                       -- alist + empty list = alist
merge2 [] ys = ys                                                                                                       -- empty list + blist = blist
merge2 (x: xs) (y: ys) = x : y : merge2 xs ys                                                                           -- merge list by recursive
                         

{- (b) merge2Tail 10% -}

merge2Tail :: [a] -> [a] -> [a]
merge2Tail [] [] = []
merge2Tail xs [] = xs
merge2Tail [] ys = ys
merge2Tail (x: xs) (y: ys) =  foldr revAppend (x : y : (merge2Tail xs ys)) []                                           -- merge list by foldr and revAppend
                                where                                                                                   -- revAppend each x and y then use foldr
                                 revAppend :: [a] -> [a] -> [a]
                                 revAppend [] acc = acc
                                 revAppend (x:xs) acc = revAppend xs (x:acc)


{- (c) mergeN 5%-}
mergeN :: [[a]] -> [a]
mergeN [[]] = []
mergeN (x: xs) = foldl merge2 x xs                                                                                      -- merge each list by foldl


-- 2
{- (a) removDuplicates 10% -}
removeDuplicates:: Eq a => [a] -> [a]
removeDuplicates [] = []
{-removeDuplicates (x: xs) = if not (x `elem` xs) then x : removeDuplicates xs
                            else removeDuplicates xs-}
removeDuplicates (x: xs) =  x: removeDuplicates (filter (/=x) xs)                                                       -- get x then use filter delete all in list then do rest as same

{- (b) count 5% -}
count :: Eq a => a -> [a] -> Int
count s [] = 0
count s (x: xs) = if not (s `elem` (x: xs)) then 0 else (count s (filter (==s) xs)) + 1                                   -- if s not in list then return 0 else use filter get all s in list and count them


{- (c) histogram 10% -}
histogram :: Eq a => [a] -> [(a, Int)]
histogram [] = []
histogram (x: xs) = (x, (count x (x: xs))) : histogram (filter (/=x) xs)                                                -- (x, number) from list. Use the method almost same as count function


-- 3                
{- (a) concatAll 4% -}
concatAll :: [[String]] -> String
concatAll [[]] = []
concatAll (x: xs) = let
                    concatAllHelper :: [String] -> String
                    concatAllHelper [] = []
                    concatAllHelper (y: ys) = foldl (++) [] (y: ys)                                                     -- concat string in list
                    in
                    foldl (++) [] (map concatAllHelper (x: xs))                                                         -- concat all list string


{- (b) concat2Either 9% -}               
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)
concat2Either:: [[AnEither]] -> AnEither
concat2Either [] = AString ""                                                                                           -- empty list ouput AString ""
concat2Either [[]] = AString ""                                                                                         -- whole list empty ouput AString ""
concat2Either (x: xs) = foldl concat2EitherHelper2 (AString "") (map concat2EitherHelper1 (x: xs))                      -- concat each list
                        where
                        concat2EitherHelper1 :: [AnEither] -> AnEither
                        concat2EitherHelper1 [] = AString ""
                        concat2EitherHelper1 (y: ys) = foldl concat2EitherHelper2 (AString "") (y: ys)                  -- concat each AnEither

                        concat2EitherHelper2 :: AnEither -> AnEither -> AnEither                                        -- calculate
                        concat2EitherHelper2 (AString s1) (AString s2) = AString (s1 ++ s2)
                        concat2EitherHelper2 (AString s1) (AnInt i2) = AString (s1 ++ show (i2))
                        concat2EitherHelper2 (AnInt i1) (AString s2) = AString (show (i1) ++ s2)
                        concat2EitherHelper2 (AnInt i1) (AnInt i2) = AString (show (i1 + i2))


{- (c) concat2Str 6% -}
concat2Str:: [[AnEither]] -> String
concat2Str [] = ""
concat2Str [[]] = ""
concat2Str (x: xs) = concat2StrHelper3 (foldl concat2StrHelper2 (AString "") (map concat2StrHelper1 (x: xs)))
                        where
                        concat2StrHelper1 :: [AnEither] -> AnEither
                        concat2StrHelper1 [] = AString ""
                        concat2StrHelper1 (y: ys) = foldl concat2StrHelper2 (AString "") (y: ys)

                        concat2StrHelper2 :: AnEither -> AnEither -> AnEither
                        concat2StrHelper2 (AString s1) (AString s2) = AString (s1 ++ s2)
                        concat2StrHelper2 (AString s1) (AnInt i2) = AString (s1 ++ show (i2))
                        concat2StrHelper2 (AnInt i1) (AString s2) = AString (show (i1) ++ s2)
                        concat2StrHelper2 (AnInt i1) (AnInt i2) = AString (show (i1 + i2))

                        concat2StrHelper3 :: AnEither -> String                                                         -- change type from AnEither to String
                        concat2StrHelper3 (AnInt i) = (show i)
                        concat2StrHelper3 (AString s) = s


-- 4
data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y = x+y
evaluate Sub x y = x-y
evaluate Mul x y = x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}
evaluateTree :: ExprTree Int -> Int
evaluateTree (ELEAF op) = op
evaluateTree (ENODE op t1 t2) = evaluate op (evaluateTree t1) (evaluateTree t2)                                         -- evaluate node from each leaves


{- (b) printInfix - 10% -}
printInfix:: Show a => ExprTree a -> String
printInfix (ELEAF op) = (show op)
printInfix (ENODE op t1 t2) = "(" ++ (printInfix t1) ++ " `" ++ (show op)++ "` " ++ (printInfix t2) ++ ")"              -- Infix order


{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)

createRTree :: ExprTree Int -> ResultTree Int
createRTree (ELEAF x) = RLEAF x

createRTreeHelper1 :: (a -> a) -> ExprTree Int -> ResultTree Int
createRTreeHelper1 op (ELEAF x) = RLEAF (op x)
createRTreeHelper1 op (ENODE v (ELEAF l) (ELEAF r)) = (RNODE (evaluate v) (createRTreeHelper1 evaluate l) (createRTreeHelper1 evaluate r))

--createRTree (ENODE op _ _) = (RNODE op _ _)
--createRTree (ENODE op (ELEAF l) (ELEAF r)) = (RNODE (createRTreeHelper1 (ENODE op l r)) (createRTree l) (createRTree r))
--
--createRTreeHelper1 :: ExprTree Int ->ResultTree Int
--createRTreeHelper1 (ELEAF x) = RLEAF x
--createRTreeHelper1 (ENODE op (ELEAF l) (ELEAF r)) = RLEAF (evaluate op l r)

--createRTree (ELEAF x) = if x /= ENODE then (RLEAF x) else (RNODE x _ _)
--createRTree (ENODE op l r) = if l == ENODE && r == RNODE then RNODE op (createRTree l) (createRTree r)
--                             else if l == ENODE && r /= ENODE then RNODE op (createRTree l) (RLEAF r)
--                             else if l /= ENODE && r == ENODE then RNODE op (RLEAF l) (createRTree r)
--                             else RNODE (evaluate op (createRTreeHelper1 l) (createRTreeHelper1 r)) (createRTreeHelper2 l) (createRTreeHelper2 r)
--                             where
--                             createRTreeHelper1 :: ExprTree Int -> Int
--                             createRTreeHelper1 (ELEAF x) = x
--
--                             createRTreeHelper2 :: ExprTree Int -> ResultTree Int
--                             createRTreeHelper2 (ELEAF x) = (RLEAF x)




--createRTree (ENODE op x y) = (RNODE (RLEAF (evaluate op x y)) (createRTreeHelper x) (createRTreeHelper y))              -- evaluate node from leave, instead op with number computed, do createRTree in leaves
--                                where
--                                createRTreeHelper :: ExprTree Int -> ResultTree Int
--                                createRTreeHelper (ELEAF op) = (RLEAF op)
--                                createRTreeHelper (ENODE op (ELEAF x) (ELEAF y)) = (RNODE (RLEAF (evaluate op x y)) (createRTreeHelper (ELEAF x)) (createRTreeHelper (ELEAF y)))
--                                createRTreeHelper (ENODE op (ELEAF x) (ENODE op1 (ELEAF x1) (ELEAF y1))) =
--                                            (RNODE (RLEAF (evaluate op x (evaluate op1 x1 y1))) (createRTreeHelper (ELEAF x)) (createRTreeHelper (ENODE op1 (ELEAF x1) (ELEAF y1))))
--                                createRTreeHelper (ENODE op (ENODE op1 (ELEAF x1) (ELEAF y1)) (ELEAF y)) =
--                                            (RNODE (RLEAF (evaluate op (evaluate op1 x1 y1) y)) (createRTreeHelper (ENODE op1 (ELEAF x1) (ELEAF y1))) (createRTreeHelper (ELEAF y)))
--                                createRTreeHelper (ENODE op (ENODE op1 (ELEAF x1) (ELEAF y1)) (ENODE op2 (ELEAF x2) (ELEAF y2))) =
--                                            (RNODE (RLEAF (evaluate op (evaluate op1 x1 y1) (evaluate op2 x2 y2))) (createRTreeHelper (ENODE op1 (ELEAF x1) (ELEAF y1))) (createRTreeHelper (ENODE op2 (ELEAF x2) (ELEAF y2))))


-- 5
{-Sample trees 4% -}
l11 = ELEAF 1                                           --                 Sub
l12 = ELEAF 2                                           --                 / \
l13 = ELEAF 3                                           --               Mul   4
l14 = ELEAF 4                                           --               / \
n11 = ENODE Add l11 l12                                 --             Add  3
n12 = ENODE Mul n11 l13                                 --             / \
t14 = ENODE Sub n12 l14                                 --            1   2

l21 = ELEAF 10                                          --                 Add
l22 = ELEAF 9                                           --                 / \
l23 = ELEAF 8                                           --                6  Mul
l24 = ELEAF 7                                           --                  /   \
l25 = ELEAF 6                                           --                Sub   Add
n21 = ENODE Sub l21 l22                                 --                / \   / \
n22 = ENODE Add l23 l24                                 --               10  9 8   7
n23 = ENODE Mul n21 n22
t24 = ENODE Add l25 n23





