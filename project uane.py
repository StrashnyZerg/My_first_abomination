import random
print('ведите, что планируете делать')
a = input()
variants = a.split('или')
print(variants)
n = len(variants)
random.seed()
i = random.randint(0, n - 1)
print(variants[i])

