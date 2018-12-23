# -*- coding: utf-8 -*-
import numpy as np

#laod files
def loadFiles(path):
    if path == 'hw3dataset\IBMdata.txt':
        # np.set_printoptions(suppress=True)
        data = np.loadtxt(path,usecols=(1,2))
        return data
    else:
        temp_data = np.loadtxt(path,dtype='str')
        data = []
        for i in range(len(temp_data)):
            data.append(temp_data[i].split(','))
            cul1 = list(set([f[0] for f in data ]))     #all out nodes
            cul2 = list(set([s[1] for s in data ]))
        # print(data)
        # print(cul1,cul2)
        return data, cul1, cul2   

# create graph for nodes
def createGraph(data, cul1, cul2):
    graph = np.matrix(np.zeros([len(cul1), len(cul2)]))
    for each_node in data:
        c1 = each_node[0]
        c2 = each_node[1]
        c1_i = cul1.index(c1)
        c2_j = cul2.index(c2)
        graph[c1_i, c2_j] += 1
    # print('graph:', graph)
    c1_matrix = np.matrix(np.identity(len(cul1)))
    c2_matrix = np.matrix(np.identity(len(cul2)))
    # print(c1_matrix,c2_matrix)
    return graph, c1_matrix, c2_matrix


def get_cul2(query):
    series = graph[cul1.index(query)].tolist()[0]
    return [cul2[x] for x in range(len(series)) if series[x] > 0 ]

def get_cul1(ad):
    series = graph.transpose()[cul2.index(ad)].tolist()[0]
    return [cul1[x] for x in range(len(series)) if series[x] > 0 ]

def cul1_simrank(q1, q2, C):
    if q1 == q2:
         return 1
    prefix = C / (graph[cul1.index(q1)].sum() * graph[cul1.index(q2)].sum())
    postfix = 0
    for ad_i in get_cul2(q1):
        for ad_j in get_cul2(q2):
            i = cul2.index(ad_i)
            j = cul2.index(ad_j)
            postfix += c2_matrix[i, j]
    return prefix * postfix
    
def cul2_simrank(a1, a2, C):
    if a1 == a2: 
        return 1
    prefix = C / (graph.transpose()[cul2.index(a1)].sum() * graph.transpose()[cul2.index(a1)].sum())
    postfix = 0
    for query_i in get_cul1(a1):
        for query_j in get_cul1(a2):
            i = cul1.index(query_i)
            j = cul1.index(query_j)
            postfix += c1_matrix[i,j]
    return prefix * postfix

def calcuSimrank(C, data, cul1, cul2, graph, c1_matrix, c2_matrix):
    # cul1 simrank
    new_c1_matrix = np.matrix(np.identity(len(cul1)))
    for qi in cul1:
        for qj in cul1:
            i = cul1.index(qi)
            j = cul1.index(qj)
            new_c1_matrix[i,j] = cul1_simrank(qi, qj, C)

    # cul2 simrank
    new_c2_matrix = np.matrix(np.identity(len(cul2)))
    for ai in cul2:
        for aj in cul2:
            i = cul2.index(ai)
            j = cul2.index(aj)
            new_c2_matrix[i,j] = cul2_simrank(ai, aj, C)

    c1_matrix = new_c1_matrix
    c2_matrix = new_c2_matrix
    return c1_matrix, c2_matrix


if __name__ == '__main__':
    '''
    following are hw3datasets
    '''
    # path = 'hw3dataset\graph_1.txt'   
    # path = 'hw3dataset\graph_2.txt'
    path = 'hw3dataset\graph_3.txt'
    # path = 'hw3dataset\graph_4.txt'
    # path = 'hw3dataset\graph_5.txt'

    #read data and create graph
    global data, c1_matrix, c2_matrix, graph, c1_matrix, c2_matrix
    data, cul1, cul2 = loadFiles(path)
    graph, c1_matrix, c2_matrix = createGraph(data, cul1, cul2)

    # print(graph,c1_matrix,c2_matrix)
    C = 0.80
    c1_matrix, c2_matrix = calcuSimrank(C, data, cul1, cul2, graph, c1_matrix, c2_matrix)
    print(c1_matrix)
