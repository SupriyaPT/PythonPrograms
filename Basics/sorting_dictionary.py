Tv = {'BreakingBad': 100, 'GameOfThrones': 100, 'TMKUC': 88}

Keymax = max(Tv, key=Tv.get)
print(Keymax)


dictkeys = list(Tv.keys())
dictvalues = list(Tv.values())

print(dictkeys[dictvalues.index(max(dictvalues))])