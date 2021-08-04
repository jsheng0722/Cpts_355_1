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
                        if op3 in dictstack[-1][0].values():
                            dict_K = list(dictstack[-1][0].keys())[list(dictstack[-1][0].values()).index(op3)]
                            dictstack[-1][0][dict_K] = str_result
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

# def stack():
#     print(list(opstack))

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
            if op2.startswith('/'):
                opPop()
                opPop()
                define(op2, op1)
            else:
                print("Error: psDef -  top of the stack is a string starting with /")
        else:
            print("111111111111111111111)"+str(op2))
            print("Error: psDef - the first operands is a non numerical value")
    else:
        print("Error: psDef expects 2 operands")

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

## Change the following functions for static scope support. 
# dictPush
def dictPush(d):
    dictstack.append(d)

# define
def define(name, value):
    if len(dictstack)==0:                           # if nothing in stack, create new as ({},0)
        dictPush(({name: value}, 0))
    else:                                           # add in currrent dict
        dictstack[-1][0][name] = value

# lookup
def lookup(name,scope):
    n = '/' + name
    if scope == "static":                                           #static scope
        try:                                                        #find the value in same position, or defined before.
            if str(n) in dictstack[staticLink(n)][0]:
                result = dictstack[staticLink(n)][0][str(n)]
                return result
        except:
            print("Can't find the static value in stack")
    elif scope == "dynamic":                                                #dynamic scope
        try:
            for i in range(len(dictstack)):                                 #find the most top one
                if str(n) in dictstack[len(dictstack) - i - 1][0]:
                    result = dictstack[len(dictstack) - i - 1][0][str(n)]
                    return result
                else:
                    continue
        except:
            print("Can't find the dynamic value in stack")
    else:
        print("Wrong scope")

# stack
def stack():
    print("==============")
    for i in range(len(opstack)):                                               # print value in list
        print(str(opstack[len(opstack) - i -1]))
    print("==============")
    for n in reversed(range(len(dictstack))):                                   # need reverse to print
        print("----" + str(n) + "----" + str(dictstack[n][1]) + "----")
        if dictstack[n][0] != {}:                                                # should not be empty dict
            for (key,value) in dictstack[n][0].items():                          # the key and value print as '---- key ---- value ----'
                print(str(key) + "    " + str(value))
        else:                                                                    #pop the empty dict
            dictPop()
    print("==============\n")

# evaluateArray
def evaluateArray(aInput):
    clear()
    for i in range(len(aInput)):
        if isinstance(aInput[i], str):
            if aInput[i] in builtinoperators:
                builtinoperators[aInput[i]]()
            elif aInput[i].startswith('(') or aInput[i].startswith('/'):
                opPush(aInput[i])
            else:
                opPush(lookup(aInput[i],'static'))
        else:
            opPush(aInput[i])
    return opstack

# Add a scope argument to the the following functions 
# psIf
def psIf():
    if len(opstack)>1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, dict):
            if isinstance(op2, bool):
                if op2:
                    interpretSPS(op1,'static')
            else:
                print("Error: it should be a boolean")
        else:
            print("Error: it should be a dict")
    else:
        print("Error: ifelse expects 3 operator")

# psIfelse
def psIfelse():
    if len(opstack)>2:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        if isinstance(op1, dict):
            if isinstance(op2, dict):
                if isinstance(op3, bool):
                    if op3:
                        interpretSPS(op2,'static')
                    else:
                        interpretSPS(op1,'static')
                else:
                    print("Error: it should be a boolean")
            else:
                print("Error: it should be a dict")
        else:
            print("Error: it should be a dict")
    else:
        print("Error: ifelse expects 3 operator")

# psFor
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
                                interpretSPS(op1, 'static')
                        else:
                            for x in range(indexStart,indexEnd - 1,op3):
                                opPush(x)
                                interpretSPS(op1, 'static')
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
# interpretSPS
# interpreter
builtinoperators = {"add": add, "sub": sub, "mul": mul, "eq": eq, "lt": lt, "gt": gt, "length": length, "get": get,
                   "getinterval": getinterval, "putinterval": putinterval, "search": search, "aload": aload, "for": psFor,
                  "astore": astore, "dup": dup, "copy": copy, "count": count, "pop": pop, "clear": clear, "exch": exch,
                   "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef, "if": psIf, "ifelse": psIfelse}
# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    l = len(dictstack) - 1                               # l be current index in dicstack
    while l >= 0 :                                       # when l >= 0, loop
        for i in dictstack[l][0]:                        # get the items in current dictstack
            if name in i:                                # if the name in items
                return l                                 # the staticLink value is l
            else:                                        # if not, do next step
                continue
        if l != 0:                                       # let the l be the value that defined before, then loop till get value or
            l = dictstack[l][1]                          #or break when not in 0
        else:
            break

#the main recursive interpreter function
def interpretSPS(tokenList,scope): # code is a code array
    # for token 'code':
    for token in tokenList['codearray']:
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
                    if i == 'length':
                        a1 = b.pop()
                        opPush(a1)
                        builtinoperators[i]()
                        r = opPop()
                        b.append(r)
                    elif i == 'dup':
                        a1 = b.pop()
                        opPush(a1)
                        builtinoperators[i]()
                        r1 = opPop()
                        r2 = opPop()
                        b.append(r1)
                        b.append(r2)
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
                    b.append(lookup(i,scope))
            opPush(b)
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
                # val = lookup(token,scope)
                val = lookup(token, scope)
                # if val is dict:
                if isinstance(val, dict):  # every time call codearray, append a empty dict
                    dictPush(({}, staticLink(token)))
                    # interpretSPS(val)
                    interpretSPS(val, scope)
                    dictPop()  # pop the empty dict
                # else:(val is not None)         \
                elif val != None:  # varable lists
                    # push val onto opstack      /
                    opPush(val)
                # else val is None:
                else:
                    # Error, undefined token
                    print("Error, undefined token: val:None")
                    print(opstack)
                    print(dictstack)
        else:
            #Error, undefined token
            print("Error, undefined token")
#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():

    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput2 = """
    /x 4 def
    (static_?) dup 7 (x) putinterval /x exch def
    /g { x stack } def
    /f { /x (dynamic_x) def g } def
    f
    """

    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """

    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n -1 1 {pop x mul} for} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """

    testinput7 = """
    /x [1 2 3 4] def
    /A { x aload pop add add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """

    testinput9 = """
        /m (0654) def
        /n (123) def m 0 n putinterval
        /o {/m true def n stack} def
        /q
            { /p { /n false def pop o} def
        	    p
        	} def
        q
        """

    testinput10 = """
        /x { 1 1 eq } def
        /n {1 2 gt 4} def
        /o { 2  n -1 1 {pop x add} for} def
        /p { /n 2 def /x 11 def o stack } def
        /q { /x 30 def /o { x 1 add } def} def
        p
        """

    testinput11 = """
        /x {(355) 1 get} def
        /e { /g (317) def} def
        /g { x stack } def
        /f { /x (322) def g } def
        f
        """

    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6,
                       testinput7, testinput8, testinput9, testinput10, testinput11]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

if __name__ == "__main__":
    sspsTests()