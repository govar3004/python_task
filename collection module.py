#          COLLECTION    MODULE             #
#1
from collections import Counter
number =[1,4,2,5,3,6,1,6,3,8,6,4,2,6,5,2,7,4]
num = Counter(number)
print(num) 
#2
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['apple']=1
ordered_dict['banana']=2
ordered_dict['cherry']=3
ordered_dict['dragonfruit']=4
ordered_dict['kiwi']=5
ordered_dict['lemon']=6
print(ordered_dict)
#3
from collections import defaultdict
defaultdict_e = defaultdict(int)
defaultdict_e['tomato']=1
defaultdict_e['onion']=2
defaultdict_e['potato']=3
defaultdict_e['carrot']=4
defaultdict_e['cabbage']=5
print(defaultdict_e)
#4
from collections import ChainMap
boy1={
    'name': 'anbu',
    'age':15,
    'standard':10,
    'city': 'pondy'
     }
boy2={
    'name': 'john',
    'age':16,
    'standard':11,
    'city': 'chennai'
     }
total = ChainMap(boy1, boy2)
print(total)



