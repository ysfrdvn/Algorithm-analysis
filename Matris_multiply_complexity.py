#matrix_1 mxn
#matrix_2 nxp
#matrix_3 = matrix_1 * matrix_2 , mxp

def get_value_from_row_col(r_1,c_1):
    t=0
    for i in range(len(r_1)):
        t = t+r_1[i] * c_1[i]
    return t

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

get_value_from_row_col(a,b)

b = [[1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8] ] #4x4
a = [[1, 2, 3, 4],[5, 6, 7, 8]] #2x4

def get_row_from_matrix(a,i):
    return a[i]
def get_col_from_matrix(a,j):
    col = []
    for row in a:
        col.append(row[j])
    #    for indis in range(len(row)):
    #        if(indis == j):
    #            col.append(row[indis])
                
    return col

get_col_from_matrix(b,1)

def matrix_multiply(m_1,m_2): #karmasıklık O(m.n.p) ,/////////// O(n^3) ise kare matristir!!!!!
   
    m = len(m_1)
    n = len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a = get_row_from_matrix(m_1,i)
            b = get_col_from_matrix(m_2,j)
            c = get_value_from_row_col(a,b)
            r[i].append(c)
    return r
b = [[1, 2, 3],[5, 6, 7],[1, 2, 3],[5, 6, 7] ] #4x4
a = [[1, 2, 3, 4],[5, 6, 7, 8]] #2x4

matrix_multiply(a,b)
