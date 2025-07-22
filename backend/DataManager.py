from DataAccess import Factory

class DataManager:
    def __init__ (self):
        factory = Factory('local')
        self.database = factory.createDataAccess()
        self.cat_num = len(self.getCategoryData())

    def getCatId(self):
        return f"T{self.cat_num:03d}"

    def getCustomData(self):
        return self.database.get('Customer')
    
    def getProductData(self):
        return self.database.get('Product')
    
    def getPurchaseData(self):
        return self.database.get('Purchase')
    
    def getCategoryData(self):
        return self.database.get('Category')
    
    def addCustomData(self, name, password, email):
        self.database.add('Customer', ['name', 'pw', 'email'], [name, password, email])
        

    def addPurchaseData(self, cid, pid, quantity):
        self.database.add('Purchase', ['cus_id', 'prod_id', 'quantity'], [cid, pid, quantity])
         

    def addProductData(self, name, price, describes, img, p_type):
        cat_id = next(
            (item['id'] for item in self.getCategoryData() if item['name'] == p_type),
            None
        )

        if cat_id is None:
            cat_id = self.getCatId()
            self.database.add('Category', ['id','name'], [cat_id, p_type])
            self.cat_num += 1
        
        self.database.add('Product', ['name', 'price', 'describes', 'img', 'cat_id'], [name, price, describes, img, cat_id])

    def getCusById(self, cus_id):
        return self.database.getById('Customer', cus_id)
    
    def getProdById(self, prod_id):
        return self.database.getById('Product', prod_id)
    
    def getPurById(self, pur_id):
        return self.database.getById('Purchase', pur_id)
        
    def getCatById(self, cat_id):
        return self.database.getById('Category', cat_id)
    
    def removeCustomData(self, cus_id):
        self.database.deleteById('Customer', cus_id)

    def removeProductData(self, prod_id):
        self.database.deleteById('Product', prod_id)

    def removePurchaseData(self, pur_id):
        self.database.deleteById('Purchase', pur_id)

    def removeCategoryData(self, cat_id):
        self.database.deleteById('Category', cat_id)

    def end(self):
        self.database.close()
                
