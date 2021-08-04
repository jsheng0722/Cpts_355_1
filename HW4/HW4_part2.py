import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)  

# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    if len(opstack) == 0:  # if no value in stack -> return None
        return None
    else:
        pop_value = opstack[len(opstack) - 1]                                        # get the top value from stack
        opstack.pop()                                                                # remove it
    return pop_value                                                                 # return value
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    if len(dictstack) == 0:                                                          # almost same as opstack
        return None
    else:
        pop_value = dictstack[-1]                                                   # the top value of dictstack
        dictstack.pop()
    return pop_value
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.

#define
def define(name, value):
    if len(dictstack)==0:                           # if nothing in stack, create new as ({},0)
        dictPush({name: value})
    else:                                           # add in currrent dict
        dictstack[-1][name] = value
    #add name:value pair to the top dictionary in the dictionary stack.
    #Keep the '/' in the name constant.
    #Your psDef function should pop the name and value from operand stack and
    #call the “define” function.

def lookup(name):
    n = '/' + name
    result = 0
    try:
        #print(dictstack)
        for i in dictstack:
            if str(n) in i:
                result = i[str(n)]
            else:
                continue
    except:
        print("Can't find the value in stack")
    return result
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if isinstance(op1, int) and isinstance(op2, int):
            opPop()
            opPop()
            opPush(op1 + op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if isinstance(op1, int) and isinstance(op2, int):
            opPop()
            opPop()
            opPush(op1 - op2)
        else:
            print("Error: sub - one of the operands is not a numerical value")
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if isinstance(op1, int) and isinstance(op2, int):
            opPop()
            opPop()
            opPush(op1 * op2)
        else:
            print("Error: mul - one of the operands is not a numerical value")
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if op1 == op2:
            opPop()
            opPop()
            opPush(True)
        else:
            opPop()
            opPop()
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if op1 < op2:
            opPop()
            opPop()
            opPush(True)
        else:
            opPop()
            opPop()
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

def gt():
    if len(opstack) > 1:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if op1 > op2:
            opPop()
            opPop()
            opPush(True)
        else:
            opPop()
            opPop()
            opPush(False)
    else:
        print("Error: lt expects 2 operands")

# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if len(opstack) > 0:
        op = opPop()
        if op.startswith('('):
            str1 = op.replace('(','').replace(')','')
            n = len(str1)
            opPush(n)
        else:
            print("Error: length need string start with (")
    else:
        print("Error: length expects 1 operands")

def get():
    if len(opstack) > 1:
        op1 = opPop()
        #print(op1)
        if isinstance(op1, int):
            op2 = opPop()
            #print(op2)
            if op2.startswith('('):
                str1 = op2.replace('(','').replace(')','')
                opPush(ord(str1[op1]))
            else:
                print("Error: get string should start with (")
        else:
            print("Error: get - the value before get shoud be int")
    else:
        print("Error: get expects 2 operands")

def getinterval():
    if len(opstack) > 2:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) & isinstance(op2, int):
            op3 = opPop()
            if op3.startswith('('):
                str1 = op3.replace('(', '').replace(')', '')
                opPush('(' + str1[op2:(op1 + op2)] + ')')
            else:
                print("Error: getinterval string should start with (")
        else:
            print("Error: getinterval - one of the operands is not a numerical value")
    else:
        print("Error: getinterval expects 3 operands")

def putinterval():
    if len(opstack) > 2:
        op1 = opPop()
        #print(op1)
        if op1.startswith('('):
            str1 = op1.replace('(', '').replace(')', '')
            op2 = opPop()
            #print(op2)
            if isinstance(op2, int):
                op3 = opPop()
                #print(op3)
                if op3.startswith('('):
                    str_id = id(op3)
                    str3 = op3.replace('(', '').replace(')', '')
                    str_result = '(' + str3[:op2] + str1 + str3[(len(str1) + op2):] + ')'
                    if len(dictstack) > 0:
                        if op3 in dictstack[-1].values():
                            dict_K = list(dictstack[-1].keys())[list(dictstack[-1].values()).index(op3)]
                            dictstack[-1][dict_K] = str_result
                    # print(result)
                    # opPush('(' + result + ')')
                    if len(opstack) > 0:
                        for i in range(len(opstack)):
                            if id(opstack[i]) == str_id:
                                opstack[i] = str_result
                else:
                    print("Error: putinterval - the inter value must start with (")
            else:
                print("Error: putinterval - the index value must be int")
        else:
            print("Error: putinterval - the inter value must start with (")
    else:
        print("Error: putinterval expects 3 operands")

def search():
    if len(opstack) > 1:
        op1 = opPop()
        #print(op1)
        op2 = opPop()
        #print(op2)
        if isinstance(op1,str):
            if op1.startswith('('):
                item = op1.replace('(','').replace(')','')
                if isinstance(op2,str):
                    if op2.startswith('('):
                        li1 = op2.split(item,1)
                        if li1[0] == op2:
                            opPush(op2)
                            opPush(False)
                        else:
                            opPush('('+ li1[1])
                            opPush(op1)
                            opPush(li1[0] + ')')
                            opPush(True)
                        # print(opstack)
                    else:
                        print("Error: search - the string must start with (")
                else:
                    print("Error: search - the value must be string")
            else:
                print("Error: search - the value of search item must start with (")
        else:
            print("Error: search - the value must be string")
    else:
        print("Error: search expects 2 operands")

# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

def evaluateArray(aInput):
    clear()
    for i in range(len(aInput)):
        if isinstance(aInput[i], str):
            if aInput[i] in builtinoperators:
                builtinoperators[aInput[i]]()
            elif aInput[i].startswith('(') or aInput[i].startswith('/'):
                opPush(aInput[i])
            else:
                opPush(lookup(aInput[i]))
        else:
            opPush(aInput[i])
    return opstack
    #should return the evaluated array

def aload():
    if len(opstack) > 0:
        op1 = opPop()
        if isinstance(op1,list):
            for i in op1:
                opPush(i)
            opPush(op1)
        else:
            print("Error: aload must 1 list")
    else:
        print("Error: aload expects 1 operands")

def astore():
    if len(opstack) > 0:
        op1 = opPop()
        number_pop = len(op1)
        try:
            for i in range(number_pop):
                j = opPop()
                op1[i] = j
            opPush(list(reversed(op1)))
        except:
            print("Error: astore - no enough value can be stored")

    else:
        print("Error: astore - expects 1 operands")

# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if len(opstack) > 0:
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        print("Error: dup expects 1 operands")

def copy():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, int):
            for i in opstack[len(opstack) - op:op + 1]:
                opPush(i)
        else:
            print("Value type should be int")
    else:
        print("Error: copy expects 1 more operands")

def count():
    opPush(len(opstack))

def pop():
    opPop()

def clear():
    for i in range(len(opstack)):
        opPop()

def exch():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        print("Error: exch expects 2 operands")

def stack():
    print(list(opstack))

# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    if isinstance(opPop(), int):
        opPush({})
    else:
        print("Error: psDict - need set the dict")

def begin():
    if opPop() == {}:
        dictPush({})
    else:
        print("Error: begin - begin without dict")

def end():
    dictPop()

def psDef():
    if len(opstack) > 1:
        op2 = opstack[-2]
        op1 = opstack[-1]
        if isinstance(op2, str):
            opPop()
            opPop()
            define(op2, op1)
        else:
            print("Error: psDef -  top of the stack is a string starting with /")
    else:
        print("Error: psDef expects 2 operands")

def psIf():
    if len(opstack)>1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, dict):
            if isinstance(op2, bool):
                if op2:
                        interpretSPS(op1)
            else:
                print("Error: it should be a boolean")
        else:
            print("Error: it should be a dict")
    else:
        print("Error: ifelse expects 3 operator")


def psIfelse():
    if len(opstack)>2:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        if isinstance(op1,dict):
            if isinstance(op2,dict):
                if isinstance(op3,bool):
                    if op3:
                        interpretSPS(op2)
                    else:
                        interpretSPS(op1)
                else:
                    print("Error: it should be a boolean")
            else:
                print("Error: it should be a dict")
        else:
            print("Error: it should be a dict")
    else:
        print("Error: ifelse expects 3 operator")

def psFor():
    if len(opstack)>3:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        op4 = opPop()
        if isinstance(op1, dict):
            if isinstance(op2, int):
                if isinstance(op3, int):
                    if isinstance(op4, int):
                        indexStart = op4
                        indexEnd = op2
                        if op3 > 0:
                            for x in range(indexStart,indexEnd + 1,op3):
                                opPush(x)
                                interpretSPS(op1)
                        else:
                            for x in range(indexStart,indexEnd - 1,op3):
                                opPush(x)
                                interpretSPS(op1)
                    else:
                        print("Error: start should be int")
                else:
                    print("Error: gap should be int")
            else:
                print("Error: end should be int")
        else:
            print("Error: it should be dict")
    else:
        print("Error: psFor exceed 2 operators")

builtinoperators = {"add": add, "sub": sub, "mul": mul, "eq": eq, "lt": lt, "gt": gt, "length": length, "get": get,
                   "getinterval": getinterval, "putinterval": putinterval, "search": search, "aload": aload, "for": psFor,
                  "astore": astore, "dup": dup, "copy": copy, "count": count, "pop": pop, "clear": clear, "exch": exch,
                   "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef, "if": psIf, "ifelse": psIfelse}
# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}

        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        elif c.startswith('['):
            a = c.replace('[', '').replace(']', '').split()
            b = []
            for i in a:
                if i.startswith('('):
                    b.append(str(i))
                elif i.startswith('-'):
                    b.append(int(i))
                elif i.isdigit():
                    b.append(int(i))
                elif isinstance(i, bool):
                    b.append(i)
                elif i == 'true':
                    b.append(True)
                elif i == 'false':
                    b.append(False)
                else:
                    b.append(i)
            res.append(b)
        elif c.startswith('('):
            res.append(c)
        elif c.startswith('-'):
            res.append(int(c))
        elif c.isdigit():
            res.append(int(c))
        else:
            res.append(c)
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        elif c.startswith('['):
            a = c.replace('[', '').replace(']', '').split()
            b = []
            for i in a:
                if i.startswith('('):
                    b.append(str(i))
                elif i.startswith('-'):
                    b.append(int(i))
                elif i.isdigit():
                    b.append(int(i))
                elif isinstance(i, bool):
                    b.append(i)
                elif i == 'true':
                    b.append(True)
                elif i == 'false':
                    b.append(False)
                else:
                    b.append(i)
            res.append(b)
        elif c.startswith('('):
            res.append(c)
        elif c.startswith('-'):
            res.append(int(c))
        elif c.isdigit():
            res.append(int(c))
        else:
            res.append(c)
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
def interpretSPS(code): # code is a code array
    # for token 'code':
    for token in code['codearray']:
        # if token is int:
        if isinstance(token,int):
            # push token to opstack
            opPush(int(token))
        #if token is bool
        elif isinstance(token,bool):
            # push token to opstack
            opPush(token)
        #else token is a dict:
        elif isinstance(token, dict):
            #push token to opstack
            opPush(token)
        #else if token is a list
        elif isinstance(token, list):
            b = []
            for i in token:
                if isinstance(i,int):
                    b.append(i)
                elif i in builtinoperators:
                    if i == 'length' or i == 'dup':
                        a1 = b.pop()
                        opPush(a1)
                        builtinoperators[i]()
                        r = opPop()
                        b.append(r)
                    elif i == 'getinterval' or i == 'putinterval':                   # those need pop 3 value(no use for 1-8)
                        a1 = b.pop()
                        a2 = b.pop()
                        a3 = b.pop()
                        opPush(a1)
                        opPush(a2)
                        opPush(a3)
                        builtinoperators[i]()
                        r = opPop()
                        b.append(r)
                    else:
                        a1 = b.pop()
                        a2 = b.pop()
                        opPush(a1)
                        opPush(a2)
                        builtinoperators[i]()
                        r = opPop()
                        b.append(r)
                elif i.startswith('('):
                    b.append(i)
                else:
                    b.append(lookup(i))
            opPush(b)
        # elif token.startswith('['):
            #evaluate the array
            # a = token.replace('[','').replace(']','').split()
            # b = []
            # for i in a:
            #     if i in builtinoperators:
            #         a1 = b.pop()
            #         a2 = b.pop()
            #         opPush(a1)
            #         opPush(a2)
            #         builtinoperators[i]()
            #         r = opPop()
            #         b.append(r)
            #     elif i.isdigit():
            #         b.append(int(i))
            #     elif i.startswith('-'):
            #         b.append(int(i))
            #     elif isinstance(i,bool):
            #         b.append(i)
            #     elif i == 'true':
            #         b.append(True)
            #     elif i == 'false':
            #         b.append(False)
            #     else:
            #         b.append(lookup(i))
            # opPush(b)
        #else if token is a str:
        elif isinstance(token, str):
            # if token is int:
            if token.isdigit():
                # push token to opstack
                opPush(int(token))
            elif token == 'true':
                opPush(True)
            elif token == 'false':
                opPush(False)
            elif token.startswith('-'):
                opPush(int(token))
            #if token is a name:
            # if token.find("/") != -1:
            elif token.startswith('/'):
                #push token to opstack
                opPush(token)
            elif token.startswith('('):
                opPush(token)
            #else token is a builtinoperator:
            elif token in builtinoperators:
                #call token
                builtinoperators[token]()
            # else:
            else:
                #val = lookup(token)
                val = lookup(token)
                #if val is dict:
                if isinstance(val,dict):
                    #interpretSPS(val)
                    interpretSPS(val)
                #else:(val is not None)         \
                elif val is not None:                # varable lists
                    #push val onto opstack      /
                    opPush(val)
                #else val is None:
                elif val is None:
                    #Error, undefined token
                    print("Error, undefined token")
        #else:
        else:
            #Error, undefined token
            print("Error, undefined token")


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))
#print(parse(['b', 'false', '{', 'a', '{', '1', '2', '}', '{', '{', '(E)', '}', 'true', '}', '}']))

input1 = """
            /square {dup mul} def   
            [3 -2 1]  aload pop
            /total 0 def 
            1 1 3 {pop square total add /total exch def} for 
            total 14 eq stack
         """

input2 = """
            /x 1 def
            /y 2 def
            /x 10 def
            /y 20 def
            0 x 1 y {add} for
            stack
        """
input3 = """
            /f {dup length} def
            [1 2 (322) (451) length]
            [1 -2 4 5 add (long) length]
            (123456)  f
            stack
         """
input4 = """
            /x 1 def
            /y 2 def
            1 dict begin
            /x 10 def
            1 dict begin /y 3 def x y end
            /y 20 def
            x y
            end
            x y
         """
input5 = """
            /sumArray 
            {0 exch aload pop count n sub -1 1 {pop add} for /n n 1 add def } def
            /x 5 def
            /y 10 def
            /n 1 def
            [1 2 3 4 x] sumArray
            [x 7 8 9 y] sumArray
            [y 11 12] sumArray
            [0 0 0] astore
            stack        
         """
input6 = """
            1 2 3 4 5 count copy 15 1 1 5 {pop exch sub} for 0 eq
            stack        
         """
input7 = """
            (CptS322 HW1_CptS355 HW2)
            dup /myclass exch def
            myclass 16 3 getinterval /c exch def
            myclass 4 c putinterval
            myclass
            stack
        """
input8 = """
           (COVID-19 Vaccine)
            dup
            ( ) search pop exch pop
            (-19) search
            {
                pop pop pop (Vaccine) eq
                { (yay) }
                { (???)  }
                ifelse
            } if
            stack
         """

input9 = """
           [1 2 3 4 5] aload /myA exch def
            count copy [0 0 0 0 0] astore
            myA eq
            stack
         """

input10 = """
            /n 5 def
            /fact {
                0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
                end 
            } def
            n fact
         """

input11 = """
          /fact{
                0 dict
                begin
                    /n exch def
                    1
                    n -1 1 {mul /n n 1 sub def} for 
                end
            } def
            6 fact
         """

