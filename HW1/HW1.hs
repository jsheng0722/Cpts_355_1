-- CptS 355 - Fall 2020  : 09/06/2020
--Jihui.Sheng
module HW1
     where

-- 1.a. biggerDate and maxDate
biggerDate::(Ord a1,Ord a2,Ord a3)=>(a3,a2,a1)->(a3,a2,a1)->(a3,a2,a1)                          -- Compare two tuples and get the tuple result
biggerDate (x3,x2,x1) (y3,y2,y1) = if x1 < y1 then (y3,y2,y1)                                   -- If x1 < y1 then tuple that include y1 bigger
                                   else if x1 > y1 then (x3,x2,x1)                              -- If x1 > y1 then tuple that include x1 bigger
                                   else if x1 == y1 && x2 < y2 then (y3,y2,y1)                  -- If x1 and y1 is same then compare x2 and y2
                                   else if x1 == y1 && x2 > y2 then (x3,x2,x1)                  -- If x2 >= y2 then get the bigger date tuple has x2
                                   else if x1 == y1 && x2 == y2 && x3 < y3 then (y3,y2,y1)      -- If x1 and y1, x2 and y2 are same, compare x3,y3
                                   else (x3,x2,x1)                                              -- x3 >= y3 then the bigger date is tuple that has x3


-- 1.b. maxDate
maxDate :: (Ord a1, Ord a2, Ord a3) => [(a3, a2, a1)] -> (a3, a2, a1)                           -- Compare the max date in a list
maxDate [] = error "no date"                                                                    -- If no date, it can't start compare
maxDate [x] = x                                                                                 -- If only one date in list, then it's max one
maxDate (x:xs) = biggerDate x (maxDate xs)                                                      -- Get the bigger date then compare to next


-- 2. ascending
ascending :: Ord t => [t] -> Bool                                                               -- Return true if it's ascending
ascending [] = True                                                                             -- Empty list is ascending
ascending [x] = True                                                                            -- List has only one element is ascending
ascending (y: x: xs) = if x >= y then (ascending xs)                                            -- If it's ascending then true
                       else False                                                               -- Else false


-- 3.a. insert
insert :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]                                           -- Insert one element into selected position
insert 0 item [] = [item]                                                                       -- If insert item into 0th position, then get [item]
insert n item [] = []                                                                           -- If insert into a empty list with non 0 position,
                                                                                                -- Then the insert will fail
insert n item (x: xs) = if n == 0 then item : (x: xs)                                           -- If n == 0 then insert item and get rest
                        else x : (insert (n-1) item xs)                                         -- Else go next and n-1


-- 3.b. insertEvery
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]                                            -- Insert elements through every selected position
insertEvery 0 item [] = error "n can't equals to 0"                                             -- Can't insert every element when it's 0
insertEvery n item [] = []                                                                      -- Insert to empty list will get empty
insertEvery n item (x: xs) = (insert n item (firstN n (x: xs))) ++ insertEvery n item (exceptFirstN n (x: xs))
                              where exceptFirstN :: (Eq t, Num t) => t -> [a] -> [a]            -- Get the rest elements after n
                                    exceptFirstN m [] = []                                      -- If list is empty, only can get empty list
                                    exceptFirstN m (y : ys) = if m /= 1 then (exceptFirstN (m-1) ys)
                                                              else ys                           -- Initialize n then loop till m == 1
                                    firstN :: (Eq t, Num t) => t -> [a] -> [a]                  -- If insert after first n elements and get rest next
                                    firstN m [] = []                                            -- Get the first n elements
                                    firstN m (x: xs) = if m /= 0 then x : (firstN (m-1) xs)    -- If list is empty, only can get empty list
                                                       else []                                  -- Initialize n then loop till n==0


-- 4.a. getSales
getSales :: (Num p, Eq t) => t -> [(t, p)] -> p                                                 -- Get the day's sales
getSales day [] = 0                                                                             -- If empty is empty then the sale is 0
getSales day (x: xs) = if (fst x) == day then (snd x) + getSales day xs                         -- Use fst get day, snd get each days sales, then sum
                       else getSales day xs                                                     -- Go next if can't find day


-- 4.b. sumSales
sumSales :: (Num p, Eq t1, Eq t2) => t1 -> t2 -> [(t1, [(t2, p)])] -> p                         -- Get the total sum of the day sales from company
sumSales company day [] = 0                                                                     -- Return sales = 0 if list is empty
sumSales company day (x: xs) = if fst x == company then (getSales day (snd x)) + sumSales company day xs
                               else sumSales company day xs                                     -- Get the company first to sum the day sales


-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]                                                              -- split elements in list by special element
split sep [] = []                                                                               -- If list is empty, return []
split sep (x: xs) = if splitSepCount sep (x:xs) >= 1 then ((splitHelper sep (x: xs)):[]) ++ nSplit sep ((splitSepCount sep (x:xs))-1) (exceptFirstN (length (splitHelper sep (x: xs))+1) (x: xs))
                    else ((splitHelper sep (x: xs)):[]) ++ (exceptFirstN (length (splitHelper sep (x: xs))+1) (x: xs)):[]
                    where exceptFirstN :: (Eq t, Num t) => t -> [a] -> [a]                      -- Get the rest elements after n
                          exceptFirstN m [] = []                                                -- If list is empty, only can get empty list
                          exceptFirstN m (y : ys) = if m /= 1 then (exceptFirstN (m-1) ys)
                                                    else ys                                     -- Initialize n then loop till m == 1
                          splitSepCount :: Eq a => a -> [a] -> Int                              -- Get the number of special elements in list
                          splitSepCount sep [] = 0                                              -- if list empty, return []
                          splitSepCount sep (x:xs) = if sep == x then splitSepCount sep xs + 1  -- If find special elements then count them
                                                        else splitSepCount sep xs               -- else element go next
                          splitHelper :: Eq a => a -> [a] -> [a]                                -- Stop when find special element
                          splitHelper sep [] = []                                               -- If list is empty, return []
                          splitHelper sep (x: xs) = if sep /= x then x: splitHelper sep xs else []-- If special element found then get list


-- 5.a. nSplit
nSplit :: (Ord a1, Num a1, Eq a2) => a2 -> a1 -> [a2] -> [[a2]]                                 -- Do a limited number of splits
nSplit sep n [] = []                                                                            -- Do no need to split a empty list
nSplit sep 0 iL = [iL]                                                                          -- If position of split is 0 then let the list be sublist
nSplit sep n (x: xs) = if n >= 1 then ((splitHelper sep (x: xs)):[]) ++ nSplit sep (n-1) (exceptFirstN (length (splitHelper sep (x: xs))+1) (x: xs))
                       else ((splitHelper sep (x: xs)):[]) ++ (exceptFirstN (length (splitHelper sep (x: xs))+1) (x: xs)):[]
                                                                                                -- Split list by n times, if split once, then n-1
                                                                                                -- The sublist is separated by split special element
                                                                                                -- Each time split, get the rest of list then do again
                       where exceptFirstN :: (Eq t, Num t) => t -> [a] -> [a]                   -- Get the rest elements after n
                             exceptFirstN m [] = []                                             -- If list is empty, only can get empty list
                             exceptFirstN m (y : ys) = if m /= 1 then (exceptFirstN (m-1) ys)
                                                       else ys                                  -- Initialize n then loop till m == 1
                             splitHelper :: Eq a => a -> [a] -> [a]                             -- Stop when find special element
                             splitHelper sep [] = []                                            -- If list is empty, return []
                             splitHelper sep (x: xs) = if sep /= x then x: splitHelper sep xs else []
                                                                                                -- If special element found then get list


