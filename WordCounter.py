# Count words in sentence

def wordCounter(string):
    print("Enter string: ")
    counts = {}
    words = string.split()

    # print(string)
    for word in words:
        if str.capitalize(word) in counts:
            counts[str.capitalize(word)] += 1
        else:
            counts[str.capitalize(word)] = 1

    return counts


print(wordCounter('My Name is Akshay Kamra and I am the first of my name'))
