import random
javab = random.randint(1,99)

hads = int(input('please give your idea: '))

while javab != hads:
    if javab < hads:
        print('javab kochec tar ast')
    else:
        print('javab bozorg tar ast')
    hads = int(input('please give your idea: '))
print(name,'barandeh shodi')
