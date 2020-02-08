'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    occurences = 0
    for i in range(len(word) - 1):
        if word[i:i + 2] == "th":
            occurences += 1
    return occurences