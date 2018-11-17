# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:54:36 2018

@author: MHA
"""
from anytree import Node, RenderTree

class MHAHeap:
    def __init__(self,array=[]):
        self.array=array
        self.heap_size=len(array)
    
    ##  Finding the parent of the ith node...
    def parent(self,i):
        return int(i/2)
    
    ##  Finding the left child of the ith node...
    def left(self,i):
        return 2*i+1
    
    ##  Finding the right child of the ith node...
    def right(self,i):
        return 2*i+2
    
    def display(self):
        node_list=[Node(self.array[i]) for i in range(self.heap_size)]
        for i in range(1,self.heap_size):
            node_list[i].parent=node_list[int((i+1)/2)-1]  ##  indexes matched for python being 0-index
        heap_tree=RenderTree(node_list[0])
        print(heap_tree)
if __name__=='__main__':
    h=[7*i for i in range(1,5)]        
    h=Heap(h)
    h.display()
