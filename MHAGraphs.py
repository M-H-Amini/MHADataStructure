# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:20:45 2018

@author: MHA
"""
import numpy as np

class MHASimpleGraph:
    def __init__(self,e,v):
        self.e=e
        self.v=v
        self.adj_matrix=np.matrix('0')
        
    def matrix(self):
        no=len(v)
        res=np.zeros((no,no))
        for i in self.e:
            res[i[0]-1,i[1]-1]=1
            res[i[1]-1,i[0]-1]=1
        self.adj_matrix=res
        return self.adj_matrix
    
if __name__=='__main__':
    v=[1,2,3,4,5]
    e=[[1,2],[1,3],[2,4],[3,5]]
    graph=MHASimpleGraph(e,v)
    
    m=graph.matrix()
    print(m)