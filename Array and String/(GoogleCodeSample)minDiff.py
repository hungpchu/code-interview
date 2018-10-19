import copy
import itertools

def solution(A):
    # using utils function function will recursively get the 2 sum that is have the least differences
    # Server 1 will be 0, server 2 will me sum of array, calling recursively till both have least differences
    S_1 = []
    S_2 = A
    differencesTable = []
    i = 0
    size = len(A)

    for subset in list(itertools.permutations(A, size)):
        S_1 = []
        S_2 = list(subset)
       # print(i, subset)
       # print(S_2)
        for s in subset:
            print("s=",s)
            S_1.append(s)
            S_2.remove(s)
            differences = abs(sum(S_1) - sum(S_2))
            differencesTable.append(differences)

        i += 1
    print(differencesTable)

    return min(differencesTable)


A = [4, 5, 3, 1, 2]
print (solution(A))
# differences =  solution(A)
# print differences
