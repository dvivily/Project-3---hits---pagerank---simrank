# -*- coding: utf-8 -*-
import numpy as np 
import operator


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

def calcuBaseRank(pageNumber):
    damping_factor = 0.15
    init_ = np.ones(pageNumber)
    BaseRank = [[damping_factor * i / pageNumber] for i in init_]
    # print(BaseRank)
    return BaseRank

def CalcuTransformMatrix(input_maxtrix):
    output_matrix = []   
    for i in range(len(input_maxtrix)):
        count = 0
        for j in range(len(input_maxtrix[i])):
            if input_maxtrix[i][j] != 0:
                count += 1
        if count != 0:                                  # average probability ...
            tran_prob = 1 / count     
        else:                                           # if one page does't have a superLink,then set it 0 ...
            tran_prob = 0
        output_matrix_tmp = []
        for j in range(len(input_maxtrix[i])):
            output_matrix_tmp.append(tran_prob * input_maxtrix[i][j])
        output_matrix.append(output_matrix_tmp)
    output_matrix = np.transpose(output_matrix) 
    return output_matrix
    
def getPR(damping_factor,Gm,Res,PR):
    Gm_PR = np.dot(Gm,PR) 
    P_Gm_PR = (1-damping_factor)*Gm_PR
    new_PR = P_Gm_PR + Res                                  #PR=P*Gm'PR*(1-d)+d/n PageRank ...
    return new_PR

def mainFunc(data):
    input_data = data
    print(input_data)
    temp_data = []
    for j in range(len(data)):
        for k in range(len(data[j])):
            temp_data.append(int(data[j][k]))
    temp_data = set(temp_data)
    maxNum = max(temp_data)                              # the number of web nodes ...
    pageNumber = maxNum                                  # calculate the total number of nodes to create the matrix...
    damping_factor = 0.15                                # set damping_factor...

    A = np.zeros((pageNumber,pageNumber))
    for l in range(len(input_data)):
        A[int(data[l][0]) - 1][int(data[l][1]) - 1] = 1
    A = np.array(A)
    print(A)
                                                         # A for dataset2
    # A =  np.array([[0,0,0,0,0,1],
    #                [1,0,0,0,0,0],
    #                [0,1,0,0,0,0],
    #                [0,0,1,0,0,0],
    #                [0,0,0,1,0,0],
    #                [0,0,0,0,1,0]])
    # A = np.transpose(A)                                 #T  
    # print(A)

    PR_ = []  
    for i in range(pageNumber):
        PR_.append([0])       
    count = 0                                           # counter...
    while True:  
        PR = PR_  
        Res = calcuBaseRank(pageNumber)
        Gm = CalcuTransformMatrix(A)
        PR_ = getPR(1-damping_factor,Gm,Res,PR)
        count = count +1
         
        # print('PR:',PR)
        # print('PR_   :',PR_)
        # print(operator.eq(np.around(PR,5) ,np.around(PR_,5 ))) 
        if operator.eq(list(np.around(PR,5)),list(np.around(PR_,5))) is True:  #set stop, when the last result equeal to this result  
            break

    for a in range(pageNumber):
        print('pageNumber ' + str(a + 1) + ' の pageRank : ' , str(round(PR_[a][0],5)) + '\t')



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
