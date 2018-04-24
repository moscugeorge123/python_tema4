import copy

f = open('m_rar_2018_5.txt', 'r')
content_file = f.read()
f.close()

precision = 1
for i in range(0, 10):
    precision /= 10

content_file_array = content_file.split('\n')
content_file_array = [a for a in content_file_array if a != '']

length = int(content_file_array[0])
content_file_array.pop(0)

B = [float(content_file_array[i]) for i in range(0, length)]

elements = [[] for i in range(0, length)]
index =  [[] for i in range(0, length)]
diagonal = []

for i in range(length, len(content_file_array)):
    tmp = content_file_array[i].split(', ')
    tmp = [float(i) for i in tmp]
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])

    if (tmp[1] == tmp[2]):
        diagonal += [tmp[0]]

    elements[tmp[1]] += [tmp[0]]
    index[tmp[1]] += [tmp[2]]


diagonal_has_0_elements = False
for i in range(0, len(diagonal)):
    if abs(diagonal[i]) < precision:
        diagonal_has_0_elements = True
        break


def equal(previous, nxt):
    for i in range(0, len(previous)):
        p = previous[i]
        n = nxt[i]

        if p != n:
            print(p, n)
            return False
    return True

def getIndex(i):
    for j in range(0, len(index[i])):
        if index[i][j] == i:
            return j
    return 0

if not diagonal_has_0_elements:
    X = [0 for i in B]
    X_prev = [i+1 for i in X]
    counter = 0

    while not equal(X_prev, X):
        for i in range(0, len(elements)):
            tmp = 0.0
            for j in range(0, len(index[i])):
                if i == index[j]:
                    continue

                tmp -= elements[i][j] * X[i]
            
            tmp += B[i]
            tmp /= elements[i][getIndex(i)]
            X[i] = tmp

        X_prev = copy.copy(X)
        counter += 1
        print(counter)
        



    