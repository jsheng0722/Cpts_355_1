import unittest
from HW3 import *

class HW3Tests(unittest.TestCase):
    def setUp(self):
        self.CDCdata = { 'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},
            'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266}, 
            'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811}, 
            'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751}, 
            'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }
        self.CDCdata1 = {
            'King': {'Mar': 3, 'Apr': 4, 'Jun': 5, 'July': 7, 'Aug': 8, 'Sep': 9},
            'Pierce': {'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'July': 7, 'Sep': 9},
            'Snohomish': {'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'July': 7, 'Aug': 8, 'Sep': 9},
            'Spokane': {'Mar': 3, 'Apr': 4, 'Jun': 6, 'July': 7, 'Aug': 8, 'Sep': 9},
            'Whitman': {'Apr': 3, 'May': 5, 'Jun': 6, 'July': 7, 'Sep': 9, 'Oct': 10}}
        self.CDCdata2 = {
            'King': {'Mar': 1, 'Apr': 1, 'May': 1, 'Jun': 1, 'July': 1, 'Aug': 1, 'Sep': 1},
            'Pierce': {'Mar': 1, 'Apr': 1, 'May': 1, 'Jun': 1, 'July': 1, 'Aug': 1, 'Sep': 1},
            'Snohomish': {'Mar': 1, 'Apr': 1, 'May': 1, 'Jun': 1, 'July': 1, 'Aug': 1, 'Sep': 1},
            'Spokane': {'Mar': 1, 'Apr': 1, 'May': 1, 'Jun': 1, 'July': 1, 'Aug': 1, 'Sep': 1},
            'Whitman': {'Apr': 1, 'May': 1, 'Jun': 1, 'July': 1, 'Aug': 1, 'Sep': 1, 'Oct': 1}}

    def test_getNumCases(self):
        self.assertEqual(getNumCases(self.CDCdata,['Whitman'],['Apr','May','Jun']),31)
        self.assertEqual(getNumCases(self.CDCdata, ['King', 'Pierce'], ['July', 'Aug']), 13587)
        self.assertEqual(getNumCases(self.CDCdata,['Snohomish','Whitman'],['Jun','July']),2178)
        self.assertEqual(getNumCases(self.CDCdata, ['Whitman', 'King'], ['Apr', 'Aug']), 8468)

    def test_getMonthlyCases(self):
        monthlyCases = {'Mar': {'King': 2706, 'Pierce': 460, 'Snohomish': 1301, 'Spokane': 147}, 'Apr': {'King': 3620, 'Pierce': 965, 'Snohomish': 1145, 'Spokane': 222, 'Whitman': 7}, 'May': {'King': 1860, 'Pierce': 522, 'Snohomish': 532, 'Spokane': 233, 'Whitman': 5}, 'Jun': {'King': 2157, 'Pierce': 647, 'Snohomish': 568, 'Spokane': 794, 'Whitman': 19}, 'July': {'King': 5014, 'Pierce': 2470, 'Snohomish': 1540, 'Spokane': 2412, 'Whitman': 51}, 'Aug': {'King': 4327, 'Pierce': 1776, 'Snohomish': 1134, 'Spokane': 1530, 'Whitman': 514}, 'Sep': {'King': 2843, 'Pierce': 1266, 'Snohomish': 811, 'Spokane': 1751, 'Whitman': 732}, 'Oct': {'Whitman': 278}}
        monthlyCases1 = {'Mar': {'King': 3, 'Pierce': 3, 'Snohomish': 3, 'Spokane': 3}, 'Apr': {'King': 4, 'Pierce': 4, 'Snohomish': 4, 'Spokane': 4, 'Whitman': 3}, 'Jun': {'King': 5, 'Pierce': 6, 'Snohomish': 6, 'Spokane': 6, 'Whitman': 6}, 'July': {'King': 7, 'Pierce': 7, 'Snohomish': 7, 'Spokane': 7, 'Whitman': 7}, 'Aug': {'King': 8, 'Snohomish': 8, 'Spokane': 8}, 'Sep': {'King': 9, 'Pierce': 9, 'Snohomish': 9, 'Spokane': 9, 'Whitman': 9}, 'May': {'Pierce': 5, 'Snohomish': 5, 'Whitman': 5}, 'Oct': {'Whitman': 10}}
        monthlyCases2 = {'Mar': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1}, 'Apr': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'May': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'Jun': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'July': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'Aug': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'Sep': {'King': 1, 'Pierce': 1, 'Snohomish': 1, 'Spokane': 1, 'Whitman': 1}, 'Oct': {'Whitman': 1}}
        self.assertDictEqual(getMonthlyCases(self.CDCdata),monthlyCases)
        self.assertDictEqual(getMonthlyCases(self.CDCdata1), monthlyCases1)
        self.assertDictEqual(getMonthlyCases(self.CDCdata2), monthlyCases2)

    def test_mostCases(self):
        self.assertEqual(mostCases(self.CDCdata),('July', 11487))
        self.assertEqual(mostCases(self.CDCdata1), ('Sep', 45))
        self.assertEqual(mostCases(self.CDCdata2), ('Apr', 5))

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        dictList1 = [{"x": 100, "y": 200, "z": True}, {"x": 2, "y": 3, "z": "found"}, {"x": 21, "y": False}, {"t": 20}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)
        self.assertEqual(searchDicts(dictList1, "t"), 20)
        self.assertEqual(searchDicts(dictList1, "x"), 21)

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        dictList2_1 = [(0, {"x": 0, "y": True, "z": "zero"}),
                       (0, {"x": 1}), (1, {"y": False}),
                     (1, {"x": 3, "z": "three"}),
                       (2, {"x": 5, "t": "found"}),
                       (3, {"x": 6}),
                       (4, {"y": False})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)
        self.assertEqual(searchDicts2(dictList2_1, "t"), "found")
        self.assertEqual(searchDicts2(dictList2_1, "x"), 5)
    
    def test_adduptoZero(self):
        numbers1 = [1,-2,3,-4,-5,6,-7,8,9,-10]
        numbers2 = list(range (-3,3))
        numbers3 = list(range (1,10))
        numbers4 = list(range (-2,6))
        numbers5 = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
        self.assertEqual(adduptoZero(numbers1,3),[[-4, -5, 9], [-2, -7, 9], [-2, -4, 6], [1, 3, -4], [1, 6, -7], [1, 9, -10]])
        self.assertEqual(adduptoZero(numbers2,4),[[-3, 0, 1, 2], [-2, -1, 1, 2]])
        self.assertEqual(adduptoZero(numbers3,2),[])
        self.assertEqual(adduptoZero(numbers4, 5), [[-2, -1, 0, 1, 2]])
        self.assertEqual(adduptoZero(numbers5, 3), [[-1, -9, 10], [-1, -6, 7], [-1, -3, 4], [2, 4, -6], [2, 7, -9], [4, 5, -9]])

    def test_getLongest(self):
        strings = ['1',['22',['333',['4444','55555',['666666']],'7777777'],'4444'],'22']
        pets=[['cat',['dog','horse'],['bird',['bunny','fish']]]]
        alph = ['a',[['b'],'c', ['d',['e']]]]
        color = ['red',[['blue'],'grey', ['black',['purple']]]]
        self.assertEqual(getLongest (strings), '7777777')
        self.assertEqual(getLongest (pets), 'horse')
        self.assertEqual(getLongest(alph), 'a')
        self.assertEqual(getLongest(color), 'purple')

    # Helper function for test_apply2nextN.
    # Creates an infinite iterator representing the sequence of even numbers starting at "init"
    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    # Helper function for test_apply2nextN. 
    # This function assumes that the first value in L is less than or equal to N.
    def getnextN(self,L,n):
        tempL = []
        for item in L:
            tempL.append(item)
            n-=1
            if n==0: break
        return tempL

    def test_apply2nextN(self):
    	#test 1
        iSequence = apply2nextN(lambda a,b:a+b, 3, iter(range(1,32)))
        self.assertEqual(iSequence.__next__(),6)
        self.assertEqual(iSequence.__next__(),15)
        self.assertEqual(iSequence.__next__(),24)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,[33, 42, 51, 60, 69, 78, 87, 31])

    	#test 2
        strIter =iter('aaaabbbbccccddddeeeeffffgggghhhhjjjjkkkkllllmmmm')
        iSequence = apply2nextN(lambda a,b:a+b, 4, strIter)
        self.assertEqual(iSequence.__next__(),'aaaa')
        self.assertEqual(iSequence.__next__(),'bbbb')
        self.assertEqual(iSequence.__next__(),'cccc')
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['dddd','eeee','ffff','gggg','hhhh','jjjj','kkkk','llll','mmmm'])

        #test3
        evens = self.OddsEvens(2)
        iSequence = apply2nextN(lambda a,b:a+b, 2, evens)

        self.assertEqual(iSequence.__next__(),6)
        upto100 = self.getnextN(iSequence,10)
        self.assertEqual(upto100,[14, 22, 30, 38, 46, 54, 62, 70, 78, 86])
        self.assertEqual(iSequence.__next__(),94)

        # test 4
        strIter1 = iter('cpts322cpts355cpts321cpts315cpts350')
        iSequence = apply2nextN(lambda a, b: a + b, 7, strIter)
        self.assertEqual(iSequence.__next__(), 'cpts322')
        self.assertEqual(iSequence.__next__(), 'cpts355')
        self.assertEqual(iSequence.__next__(), 'cpts321')
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest, ['cpts315','cpts350'])

        # test 5
        iSequence = apply2nextN(lambda a,b:a+b, 2, iter(range(-10,11)))
        self.assertEqual(iSequence.__next__(), -19)
        self.assertEqual(iSequence.__next__(), -15)
        self.assertEqual(iSequence.__next__(), -11)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest, [-7,-3,1,5,9,13,17,10])

if __name__ == '__main__':
    unittest.main()

