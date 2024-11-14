def bubbleSort(lst):
    needNextPass = True
    k = 1

    while k < len(lst) and needNextPass:
        needNextPass = False
        for i in range(len(lst) - k):
            if lst[i] > lst [i+1]:
                lst[i], lst[i+1] = lst[i + 1], lst[i]
                needNextPass = True

        k+=1

def main():
    lst = [1,2,2,5,6,1,-2,3,14,12]
    bubbleSort(lst)
    for v in lst:
        print(v, end= " ")

main()