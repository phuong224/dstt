from Utils import ShoppingMatrix

class AccountManager:
    def __init__ (self):
        self.id = None
    
    def setAccount(self, id):
        self.id = id

    def setDefault(self):
        self.id = None
    
    def getPreviousProduct(self, product, purchase):
        return [] if self.id is None else [
                {
                    'product': next(prod for prod in product if prod['id'] == pur['prod_id']),
                    'pur_id': pur['id'],
                    'quantity': pur['quantity']
                }
                    for pur in purchase if pur['cus_id'] == self.id
            ]

    
    def getProposeProduct(self, custom, product, purchase, k):
        return [] if self.id is None else [
            prod 
                for srt_prod_id in ShoppingMatrix(
                    [cus['id'] for cus in custom],
                    [prod['id'] for prod in product],
                    [(pur['cus_id'], pur['prod_id'], pur['quantity']) for pur in purchase],
                    k
                ).getRow(self.id, k)
                for prod in product
                if prod['id'] == srt_prod_id
            ]
    
