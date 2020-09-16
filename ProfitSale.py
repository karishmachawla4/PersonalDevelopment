# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

prices = [1,2,3,4,5]

counter = 0
profit = 0
# j = 1
profitValues = {}
results = {}
length = len(prices)

maxVal = max(prices)
maxIndex = prices.index(maxVal)

minVal = min(prices)
minIndex = prices.index(minVal)

profits = []
buys = []
sales = []

i = 0
j = 0
while i < length:
    j = i + 1
    # print(prices[i])
    while j < length:
        # print('val of j ',prices[j])
        if prices[j] > prices[i]:
            # profits = prices[j] - prices[i]
            profits.append(prices[j] - prices[i])
            buys.append(str(i)+str(j))
            sales.append(j)
            # results.update({str(i)+str(j): profits})
        else:
            pass
        j += 1
    i += 1
# print(profitValues)
# print(prices)
print(profits)
print(buys)
biprofit = max(profits)
biind = profits.index(biprofit)
bibuys = str(buys[biind])
for a in range(len(profits)):
    b = a+1
    while b < len(profits):
        profitValues.update({buys[a]+buys[b] : profits[a]+profits[b]})
        b += 1
print(profitValues)
finalval = []
finalkey = []
for key, values in profitValues.items():
    if key[1] < key[2] < key[3]:
        finalval.append(values)
        finalkey.append(key)

print(finalkey)
print(finalval)

if max(finalval) < biprofit:
    print('Max Profit is ', biprofit)
    for kam in range(len(bibuys)):
        if kam % 2 == 0:
            print('Buy on day ', int(bibuys[kam]) + 1)
        else:
            print('Sell on ', int(bibuys[kam]) + 1)
else:
    print('Max Profit is ', max(finalval))
    maxind = finalval.index(max(finalval))
    keys = finalkey[maxind]
    for kam in range(len(keys)):
        if kam % 2 == 0:
            print('Buy on day ', int(keys[kam])+1)
        else:
            print('Sell on ', int(keys[kam])+1)