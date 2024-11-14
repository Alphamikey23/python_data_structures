# Opening with Obama said Not bubble sort - youtube.com/watch?v=k4RRi_ntQc8
# Why we need sorting algorithms? Problem solving, Fundamental programming techniques, performance

#insertion sort : 2, 9 , 5, 4, 8, 1, 6

def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i-1
        while k >=0 and lst[k] > currentElement:
            lst[k+1] = lst[k]
            k -=1


        lst[k+1] = currentElement

def main():
    list = [2,3,2,5,6,1,-2,3,14,12]
    insertionSort(list)
    for v in list:
        print(v,end=" ")

main()