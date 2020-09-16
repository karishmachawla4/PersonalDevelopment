# In python code, given a json object with nested objects, write a function that flattens all the objects to a single key
# value dictionary. Do not use the lib that actually performs this function. { a:{b:c,d:e} } becomes {a_b:c, a_d:e} ( not, a:"b:c,d:e" }


test = {'India': {'Maha': 'Mumbai', 'Guj': 'Gandhi'}}


def flatten(dictinput):
    res = {}
    for key, value in dictinput.items():
        if type(value) is dict:
            for key1, value1 in value.items():
                res.update({key + '_' + key1: value1})
        else:
            pass

    return res


print(flatten(test))

# test = {'India': {'Maha': 'Mumbai', 'Guj': 'Gandhi'}, 'USA' : {'AL': 'Montg', 'IL': 'Chic'}}
# def flatten(input):
#     result = {}
#     for key, value in test.items():
#         # print(key)
#         # print(value)
#         if type(value) is dict:
#             for key1, value1 in value.items():
#                 # print(value)
#                 # print(key)
#                 print(key1)
#
#             result = { key+'_'+key1: value1 for key in key1 }
#         else:
#             pass
#
#     return result
#
# print(flatten(test))
