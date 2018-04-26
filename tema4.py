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
index = [[] for i in range(0, length)]
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

elements = [[12, 3, -5], [1, 5, 3], [3, 7, 13]]
index = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
B = [1, 28, 76]

diagonal_has_0_elements = False
for i in range(0, len(diagonal)):
    if abs(diagonal[i]) < precision:
        diagonal_has_0_elements = True
        break


def equal(previous, nxt):
    for i in range(0, len(previous)):
        p = previous[i]
        n = nxt[i]

        if abs(p) - abs(int(p)) < precision or 1 - (abs(p) - abs(int(p))) < precision:
            p = int(p)

        if abs(n) - abs(int(n)) < precision or 1 - (abs(n) - abs(int(n))) < precision:
            n = int(n)
        # print(p, n)
        if p != n:
            # print(previous, nxt)
            return False
    return True


def getIndex(i):
    for j in range(0, len(index[i])):
        if index[i][j] == i:
            return j
    return 0


if not diagonal_has_0_elements:
    X = [0, 0, 0]  # [0 for i in B]
    X_prev = [i + 1 for i in X]
    counter = 0

    while not equal(X_prev, X):
        X_prev = copy.copy(X)
        for i in range(0, len(elements)):
            tmp = B[i]

            for j in range(0, len(index[i])):
                if i == index[i][j]:
                    continue

                tmp -= elements[i][j] * X[index[i][j]]
                # print("elements", elements[i][j], X[index[i][j]])

            tmp /= elements[i][getIndex(i)]
            # print("tmp", tmp, B[i])
            # print(X[i], B[i], elements[i][getIndex(i)], tmp)
            X[i] = tmp

        counter += 1
        print(counter)
    print(X)
