dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':4,'e':5,'f':6}

merge_dict = {
    **{ k: v for k,v in dict1.items() if k in 'aeiou'},
              **{k: v for k,v in dict2.items() if k in 'aeiou'}}

print(merge_dict)
print(dict1.items())
print(dict2.items())

