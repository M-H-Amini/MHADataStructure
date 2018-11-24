# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:20:45 2018

@author: MHA
"""
import numpy as np
import queue
import cv2

class MHASimpleGraph:
    def __init__(self,e,v):
        self.e=e
        self.v=v
        self.adj_matrix=np.matrix('0')
        self.seen_list=[]
        self.path_list=[]
        
    def matrix(self):
        no=len(v)
        res=np.zeros((no,no))
        for i in self.e:
            res[i[0],i[1]]=1
            res[i[1],i[0]]=1
        self.adj_matrix=res
        return self.adj_matrix
    
    ##  Finding the adjacents of a node...
    def adj(self,s):
        res=[]
        for i in range(len(self.v)):
            if self.adj_matrix[s,i]:
                res.append(i)
        return res
    
    def bfs(self,s):
        self.path_list=[]
        self.seen_list=[]
        used_list=[]
        temp_queue=queue.Queue()
        temp_queue.put(s)
        while not temp_queue.empty():
            #print('qsize---{}'.format(temp_queue.qsize()))
            temp_node=temp_queue.get()
            used_list.append(temp_node)
            #print('temp_node---{}'.format(temp_node))
            #print('qsize---{}'.format(temp_queue.qsize()))
            self.seen_list.append(temp_node)
            #print('seen_list---{}'.format(self.seen_list))
            for i in self.adj(temp_node):
                #print('adj---{}'.format(i))
                if i not in used_list:
                    temp_queue.put(i)
                    used_list.append(i)
                    self.path_list.append([temp_node,i])
                    #print('added---{}'.format(i))
    
    #  Find the index of the group in path_list in which the 'index'th 
    def findIndex(self,path_list,a,index):
        for i in range(len(path_list)):
            if path_list[i][index]==a:
                return i
    
    def shortestPath(self,a,b):
        self.bfs(a)
        path=[b]
        goal=b
        while True:
            goal=self.findIndex(self.path_list,goal,1)
            goal=self.path_list[goal][0]
            if goal!=a:
                path.append(goal)
            else:
                path.append(goal)
                break
        result=[0 for i in range(len(path))]
        for i in range(len(path)):
            result[i]=path[len(path)-i-1]
        return result
        
if __name__=='__main__':
    v=[i for i in range(10)]
    e=[[0,1],[0,2],[1,3],[2,4],[6,1],[7,1],[2,5],[5,6],[6,9],[6,8],[7,8]]
    graph=MHASimpleGraph(e,v)
    m=graph.matrix()
    graph.bfs(5)
    #print(graph.seen_list)
    path=graph.shortestPath(3,9)
    print(path)