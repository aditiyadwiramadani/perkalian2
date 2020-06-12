import numpy as np 


def kalian():
		x = np.array([[4,5],  
		              [8,9]])
		              
		y  =  np.array([[2,5],
		               [5,6]])
		return x @ y


'''
rumus    a = 4 * 2 + 5 * 5  dan  4 * 5 + 5 * 6
         b = 8 * 2 + 9 * 5  dan  8 * 5 + 9 * 6 
         
   
'''

print (kalian())



#print(tiga2())
