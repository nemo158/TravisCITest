#coding='utf-8'
import numpy as np

def multiply_print(a,b):
    print("-------------------\n输入a矩阵为：")
    print(a)
    print("输入b矩阵为：")
    print(b)
    #a = np.array([[1],[1],[1]])
    #b = np.array([1,2])
    x=np.multiply(a,b)
    print("输出矩阵x为：")
    print(x)
    print("-------------------")
    return x

