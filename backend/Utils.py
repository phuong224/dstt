import numpy as np
from typing import List, Tuple

class SVD:
    @staticmethod
    def svd_decompose(matrix):
        U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
        return U, S, Vt
    
    @staticmethod
    def svd_reconstruct(U, S, Vt):
        S_matrix = np.diag(S)
        return np.dot(U, np.dot(S_matrix, Vt))
    
    @staticmethod
    def svd_reduce(U, S, Vt, k):
        U_k = U[:, :k]
        S_k = S[:k]
        Vt_k = Vt[:k, :]
        return U_k, S_k, Vt_k
    
    @staticmethod
    def calc(matrix, k):
        U, S, Vt = SVD.svd_decompose(matrix)
        U_k, S_k, Vt_k = SVD.svd_reduce(U, S, Vt, k)
        return SVD.svd_reconstruct(U_k, S_k, Vt_k)
    
class ShoppingMatrix:
    def __init__ (self, cus_id: List[str], prod_id: List[str], purchase: List[Tuple[str, str, float]], k :int):
        self.k = k
        self.cus_map = {cus: idx for idx, cus in enumerate(cus_id)}
        self.prod_map = {prod: idx for idx, prod in enumerate(prod_id)}
        self.prods = prod_id

        self.matrix = np.zeros((len(cus_id), len(prod_id)))

        for cus, prod, value in purchase:
            if cus in self.cus_map and prod in self.prod_map:
                self.matrix[self.cus_map[cus]][self.prod_map[prod]] += value

    def getRow(self, id, num):
        n_matrix = SVD.calc(self.matrix, self.k)
        products = n_matrix[self.cus_map[id]]

        prodrec = []
        for idx, score in enumerate(products):
            if self.matrix[self.cus_map[id]][idx] == 0:
                prodrec.append((score, idx))

        sorted_prod = sorted(prodrec, key=lambda x: x[0], reverse=True)

        res = []
        for i in range (min(num, len(sorted_prod))):
            score, idx = sorted_prod[i]
            res.append(self.prods[idx])
            

        return res