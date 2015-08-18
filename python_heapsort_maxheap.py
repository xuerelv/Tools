# -*- coding: utf-8 -*-  


def leftChild(index):
    return index*2+1
def rightChild(index):
    return index*2+2

#从index开始，向后构造最大堆
def maxHeap(array, index, heapSize):
    leftInd = leftChild(index)
    rightInd = rightChild(index)
    
    largest = index
    if leftInd < heapSize and array[largest] < array[leftInd]:
        largest = leftInd
    
    if rightInd < heapSize and array[largest] < array[rightInd]:
        largest = rightInd
    
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        maxHeap(array,largest,heapSize)
    
def buildHeap(array):
    for i in range(len(array)/2,-1,-1):
        maxHeap(array,i,len(array))

def heapSort(array):
    buildHeap(array)
    for i in range(len(array)-1,0,-1):
        array[0], array[i] = array[i], array[0]
        maxHeap(array,0,i)
    
arr=[1,2,7,4,34,25,67]
heapSort(arr)
print arr
