# In python code, given a json object with nested objects, write a function that flattens all the objects to a single key
# value dictionary. Do not use the lib that actually performs this function. { a:{b:c,d:e} } becomes {a_b:c, a_d:e} ( not, a:"b:c,d:e" }


test = {'India': {'Maha': 'Mumbai', 'Guj': 'Gandhi'}}
def flatten(input):
    res = {}
    for key, value in test.items():
        if type(value) is dict:
            for key1, value1 in value.items():
                res.update({key+'_'+key1: value1})
        else:
            pass

    return res

print(flatten(test))
