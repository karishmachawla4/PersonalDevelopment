#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

def data():
    i = 0
    j = 0
    data = []
    for i in range(100):
        for j in range(5):
            data.append(i)
    return data

import time
start = time.clock()
print(start)
sorted = data()
len = len(sorted)
updLen = len
i = 0
j = 1
while i < updLen-1:
    if sorted[i] == sorted[j]:
        sorted.remove(sorted[j])
        updLen -= 1
    else:
        i += 1
        j += 1

end = time.clock()
print(end)
print(end-start)
print(sorted)