# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Name: Jihui.Sheng
#------------------------- 10% -------------------------------------
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

#-------------------------- 16% -------------------------------------
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

def define(name, value):
    if len(dictstack) == 0:
        dictstack.append({name: value})
    else:
        dictstack[-1][name] = value
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    n = '/' + name
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

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op1 + op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op1 - op2)
        else:
            print("Error: sub - one of the operands is not a numerical value")
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op1 * op2)
        else:
            print("Error: mul - one of the operands is not a numerical value")
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if op1 < op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq expects 2 operands")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if op1 > op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: lt expects 2 operands")

#--------------------------- 20% -------------------------------------
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


#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

def evaluateArray(aInput):
    operations = {"add": add, "sub": sub, "mul": mul, "eq": eq, "lt": lt, "gt": gt, "length": length, "get": get,
                   "getinterval": getinterval, "putinterval": putinterval, "search": search, "aload": aload,
                  "astore": astore, "dup": dup, "copy": copy, "count": count, "pop": pop, "clear": clear, "exch": exch,
                   "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef}
    clear()
    for i in range(len(aInput)):
        if isinstance(aInput[i], str):
            if aInput[i] in operations:
                operations[aInput[i]]()
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

#--------------------------- 6% -------------------------------------
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
    print(opstack)

#--------------------------- 20% -------------------------------------
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
    for i in range(len(dictstack)):
        if dictPop() == {}:
            break

def psDef():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op2.startswith('/'):
            dictstack.append({op2: op1})
        else:
            print("Error: psDef -  top of the stack is a string starting with /")
    else:
        print("Error: psDef expects 2 operands")
