print("\n")
print("\tBonjou, bonswa tout moun,")
print("\tPwogram sila a, se battle dat 3 desanm lan.")
def minter(entèval):
    intert = sorted(entèval, key=lambda x: x[0])
    all = [intert[0]]
    for entèv in intert:
        if entèv[0] <= all[-1][1]:
            all[-1][1] = max(all[-1][1], entèv[1])
        else:
            all.append(entèv)
    return all
entèval = [[1,4], [3,6]]
rezilta = minter(entèval)
print("\t" + str(rezilta))
print("\tMèsi")
