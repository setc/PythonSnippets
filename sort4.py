def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])
        # the questions below refer to this point, assuming we set L = lst[:] here
        print(front)
        print(back)
        print(lst)
        return unite(front, back)

lista=[6,3,2,13,7,9,10,12,4,15,8,5,14,1,11]

lista2=sort4(lista)
print(lista2)
