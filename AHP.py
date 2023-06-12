import numpy as np

criterias_rank = {
    "character" : 3,
    "relationship" : 2,
    "networth" : 1
}
alt_details = {
    "Jones Marshall" : {
        "relationship" : 3,
        "character" : 5,
        "networth" : 1000000
    },
    "Jenna Marshall" : {
        "relationship" : 3,
        "character" : 4,
        "networth" : 700000
    },
    "Peter Marshall" : {
        "relationship" : 2,
        "character" : 3,
        "networth" : 50000
    },
    "Penelope Marshall" : {
        "relationship" : 2,
        "character" : 1,
        "networth" : 500000
    },
    "Will Marshall" : {
        "relationship" : 1,
        "character" : 2,
        "networth" : 10000
    }
}
criterias = list(criterias_rank.keys())
alternatives = list(alt_details.keys())


ri_dict = {
    1:0,
    2:0,
    3:0.52,
    4:0.89,
    5:1.11,
    6:1.25,
    7:1.35,
    8:1.40,
    9:1.45,
    10:1.49
}


def print_matrix(title, arr):
    print(f'\n{title}')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(str(format(arr[i][j], '.3f')) + " | ", end="")
        print()

def print_info(title, criterias_, arr):
    print(f'\n{title}')
    for i in range(len(arr)):
        print(f'{criterias_[i]} : {round(abs(arr[i]*100), 2)}%')

def pairwise_matrix(criterias_, mode = "criterias"):
    n = len(criterias_)
    # create pairwise matrix
    A = np.ones([n,n])
    for i in range(0, n):
        for j in range(0, n):
            if i<j:
                # criterias rank
                if mode == "criterias":
                    aij = criterias_rank.get(criterias_[i]) / criterias_rank.get(criterias_[j])
                # relationship, character rank
                elif mode in criterias:
                    aij = alt_details.get(criterias_[i]).get(mode) / alt_details.get(criterias_[j]).get(mode)
                else:
                    raise NotImplementedError
                print(f'Importance of {criterias_[i]} over {criterias_[j]}: {aij}')
                A[i,j] = float(aij)
                A[j,i] = 1/float(aij)
    
    # computing the priority vector: first column of eigenvector
    eig_vec = np.linalg.eig(A)[1][:,0]
    priority_vector = eig_vec / eig_vec.sum()
    
    # compute lambda matrix
    lambda_max = np.linalg.eig(A)[0].max()
    
    # compute CI
    CI = (lambda_max - n) / (n - 1)
    CR = CI / ri_dict[n]
    
    print_matrix('Criterias Matrix', A)
    print_info('Priority Vector', criterias_, priority_vector)
    print(f'Consistency Ratio: {round(abs(CR*100), 2)}% {"< 10% (Acceptable)" if CR<0.1 else "> 10% (Not Acceptable)"}')
    
    return priority_vector

def alternative_matrix(criterias, alternatives):
    col = len(alternatives)
    row = len(criterias)
    priority_vector_matrix = np.ones([row,col])
    for i in range(len(criterias)):
        print(f'\nLevel 2 Matrix with respect to Factor: "{criterias[i]}"')
        print('-------------------------------------------------------')
        priority_vector = pairwise_matrix(alternatives, mode=criterias[i])
        
        for j in range(len(priority_vector)):
            priority_vector_matrix[i][j] = float(priority_vector[j])
        
        print()
        
    return priority_vector_matrix



if __name__ == "__main__":
    p = pairwise_matrix(criterias)
    priority_vector_matrix = alternative_matrix(criterias, alternatives)
    res = np.dot(priority_vector_matrix.T, p)
    final_selection = alternatives[np.argmax(res)]
    print_info("Alternatives Priority Vectors", alternatives, res)
    print("\nYour final result should be: ", final_selection)