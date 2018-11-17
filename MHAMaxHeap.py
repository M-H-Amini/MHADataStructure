# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:40:21 2018

@author: MHA
"""

from MHAHeap import MHAHeap as Heap

class MHAMaxHeap(Heap):
    def __init__(self,array=[]):
        Heap.__init__(self,array)
    
    def maxHeapify(self,i):
        if self.left(i)<self.heap_size and self.array[self.left(i)]>self.array[i]:
            largest=self.left(i)
        else:
            largest=i
        if self.right(i)<self.heap_size and self.array[self.right(i)]>self.array[largest]:
            largest=self.right(i)
        if largest!=i:
            temp=self.array[i]
            self.array[i]=self.array[largest]
            self.array[largest]=temp
            self.maxHeapify(largest)
    
    def buildMaxHeap(self):
        for i in range(int(self.heap_size/2),-1,-1):
            self.maxHeapify(i)
        
if __name__=='__main__':
    a=[20,30,19,40,20,15,14,50,1]  ##  Initial wrong MaxHeap...
    mx=MHAMaxHeap(a)
    mx.buildMaxHeap()
    mx.display()