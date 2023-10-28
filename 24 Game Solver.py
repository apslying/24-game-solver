def main():
    n1=float(input('Enter first number:'))
    n2=float(input('Enter second number:'))
    n3=float(input('Enter third number:'))
    n4=float(input('Enter fourth number:'))
    if 24 in game24(n1,n2,n3,n4) or 23.99999999999999 in game24(n1,n2,n3,n4):
        print('Equals 24.')
    else:
        print('Not')

def game24(a,b,c,d):
    list1=[a,b,c,d]
    listop=['+','-','*','/']
    list4=[]
    for n in range(0,4):
        for m in range(0,4):
            for op1 in listop:
                if n==m:
                    pass
                else:
                    try:
                        new=(eval(str(list1[n])+op1+str(list1[m])))
                        list2=[]+list1
                        list2.remove(list1[n])
                        list2.remove(list1[m])
                        list2.append(new)
                        for p in range(0,3):
                            for q in range(0,3):
                                for op2 in listop:
                                    if p==q:
                                        pass
                                    else:
                                        try:
                                            new2=(eval(str(list2[p])+op2+str(list2[q])))
                                            list3=[]+list2
                                            list3.remove(list2[p])
                                            list3.remove(list2[q])
                                            list3.append(new2)
                                            for op3 in listop:
                                                try:
                                                    final1=(eval(str(list3[0])+op3+str(list3[1])))
                                                    list4.append(final1)
                                                except ZeroDivisionError:
                                                    pass
                                                try:
                                                    final2=(eval(str(list3[1])+op3+str(list3[0])))
                                                    list4.append(final2)
                                                except ZeroDivisionError:
                                                    pass
                                        except ZeroDivisionError:
                                            pass
                    except ZeroDivisionError:
                        pass
    return list4

main()
