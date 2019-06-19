import itertools


list1 = ['a','b','c']
list2 = [1,2,3]


list3 = []
for l in list1:
    for b in list2:
        list3.append(l + str(b))
print(list3)


# more than two series and want true tuples
coffee = ['Latte','Cappuccino','Filter']
flavor = ['Hazelnut','Vanilla','Mocha']
milk = ['no milk','skim','2%']

for element in itertools.product(coffee, flavor, milk):
    print(element)
