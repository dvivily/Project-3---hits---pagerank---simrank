# -*- coding: utf-8 -*-
import numpy as np 
import operator
import math

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
        return data

# create transform matrix
def init_weight(pageNumber):
    weight = np.ones((pageNumber,1))
    # print('weight',weight)
    return weight

# calculate authority
def calcuAuthority(At, weight):
    v = np.dot(At,weight)
    return v

# calculate hub
def calcuHub(A,v):
    u = np.dot(A,v)
    return u

# show results
def show(v_, u_):
    for n in range(len(v_)):
        print('authority : node ' + str(n + 1) + ' :', v_[n])
    for m in range(len(u_)):
        print('hub : node ' + str(m + 1) + ' :', u_[m])


def mainFunc(data):
    input_data = data
    # print(input_data)
    temp_data = []
    for j in range(len(data)):
        for k in range(len(data[j])):
            temp_data.append(int(data[j][k]))
    temp_data = set(temp_data)
    pageNumber = max(temp_data)                              # the number of nodes ...

    A = np.zeros((pageNumber,pageNumber))
    for l in range(len(input_data)):
        A[int(data[l][0]) - 1][int(data[l][1]) - 1] = 1
    A = np.array(A)
    # print('A:',A)

    At = np.transpose(A)
    # print('At:',At)
    weights = init_weight(pageNumber)
    v_ = calcuAuthority(At, weights)
    u_ = calcuHub(A,v_)
    counter = 1
    # print('k = ', counter)
    # show(v_, u_)

    counter += 1
    while True:
        # print('k = ', counter)
        # print(math.sqrt(np.sum(v_**2)))
        # print(math.sqrt(np.sum(u_**2)))
        v_ = v_ / (math.sqrt(np.sum(v_**2)))
        u_ = u_ / (math.sqrt(np.sum(u_**2)))
        # show(v_, u_)

        counter += 1
        # print('k = ', counter)
        # print(math.sqrt(np.sum(v_**2)))
        # print(math.sqrt(np.sum(u_**2)))
        v_new = v_ / (math.sqrt(np.sum(v_**2)))
        u_new = u_ / (math.sqrt(np.sum(u_**2)))
        

        if operator.eq(list(np.around(v_new,5)),list(np.around(v_,5))) is True and operator.eq(list(np.around(u_new,5)),list(np.around(u_,5))) is True:  #set stop
            show(v_, u_)
            break
        else:
            v_ = v_new
            u_ = u_new
            counter += 1

if __name__ == '__main__':  
    '''
    following are hw3datasets
    '''
    # path = 'hw3dataset\graph_1.txt'   
    # path = 'hw3dataset\graph_2.txt'
    path = 'hw3dataset\graph_3.txt'
    # path = 'hw3dataset\graph_4.txt'
    # path = 'hw3dataset\graph_5.txt'
    # path = 'hw3dataset\graph_6.txt'

    '''
    following are project one IBM datasest
    '''
    # path = 'hw3dataset\IBMdata.txt'   
     
    '''
    following are hw3datasets_cg
    '''
    # path = 'hw3dataset\graph_1_cg.txt'   
    # path = 'hw3dataset\graph_2_cg.txt'
    # path = 'hw3dataset\graph_3_cg.txt'

    #load datasets and calculate results  
    data_ = loadFiles(path)
    mainFunc(data_)

