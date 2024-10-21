set1 = {'roger', 'syd'}
set2 = {'roger', 'lina', 'kola'}
set3 = {'roger', 'lina', 'kola', 'syd'}

intersect = set1 & set2
union = set1 | set2
diff = set1 - set2
superset = set3 > set2
subset = set1 < set3
print(intersect, union, diff, superset, subset)

# casting
print(list(set3))