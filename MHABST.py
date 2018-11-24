# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 00:04:57 2018

@author: MHA
"""

from MHAHeap import MHAHeap

class MHABST(MHAHeap):
    def __init__(self,array=[]):    
        MHAHeap.__init__(self)
        self.create(array)
        
    def create(self,array):
        self.heap_size=0
        if len(array)!=0:
            for i in array:
                self.insert(i)
        
    def insert(self,x):
        if self.heap_size==0:
            self.array=[x]
            self.heap_size=1
        else:
            p=0
            while p<self.heap_size:
                if self.array[p]==-1:
                    break
                else:
                    if x>self.array[p]:
                        p=self.right(p)
                    elif x<self.array[p]:
                        p=self.left(p)
                    elif x==self.array[p]:
                        break
                if p>=self.heap_size:
                    for i in range(self.heap_size+1):
                        self.array.append(-1)
                        self.heap_size+=1
            self.array[p]=x
            
    def search(self,x):
        if self.heap_size==0:
            self.array=[x]
            self.heap_size=1
            print('Empty! Nothing to search!!!')
            return 0
        else:
            p=0
            while p<self.heap_size:
                if self.array[p]==-1:
                    break
                else:
                    if x>self.array[p]:
                        p=self.right(p)
                    elif x<self.array[p]:
                        p=self.left(p)
                    elif x==self.array[p]:
                        print('Found!!!')
                        return 1
                        break
        print('Not found!!!')
        return 0
if __name__=='__main__':
    import numpy as np
    bst=MHABST([13,49,94,23,0,1])
    print(bst.array)
    bst.display()
    bst.search(10)