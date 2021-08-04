m any = let
            h v iL = length(filter (\x ->(x==v)) iL)
            in
            map (\x -> (x,h x any)) any

def sub1():
     global p
     z =6
     x=7
     p=8
     print(z)
     print(x)
     print(p)
     def sub2():
         global y
         nonlocal x
         x =9
         y=13
         print(x)
         print(y)
         def sub3():
             global q
             q=10
             x=12
             y=14
         sub3()
         print(q)
         print(x)
         print(y)
     sub2()
     print(x)
     print(y)