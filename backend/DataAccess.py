from abc import ABC, abstractmethod
from typing import List, Dict, Any
import mysql.connector as connector
import json, os, uuid
from functools import reduce


class DataAccess(ABC):
    @abstractmethod
    def get(self, entity: str) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def add(self, entity: str, col: List[str], val: List[str]):
        pass

    @abstractmethod
    def deleteById(self, entity: str, id: str):
        pass

    @abstractmethod
    def getById(self, entity: str, id: str):
        pass

    @abstractmethod
    def close(self):
        pass

class MySQLServerAccess(DataAccess):
    def __init__ (self):
        self.conn = connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='shop_svd'
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get(self, entity: str):
        try:
            query = f"SELECT * FROM {entity}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except connector.Error as err:
            print(f"Error: {err}")

    def add(self, entity: str, col: List[str], val: List[str]):
        try:
            res = reduce(
                lambda acc, x: acc + ", " + (f"'{x}'" if type(x) == str else f"{x}"), 
                val[1:], 
                f"'{val[0]}'" if type(val[0]) == str else f"{val[0]}"
                )
            query = f"INSERT INTO {entity} ({', '.join(col)}) VALUES ({res})"
            self.cursor.execute(query)
            self.conn.commit()
        except connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()

    def deleteById(self, entity, id):
        try:
            query = f"DELETE FROM {entity} WHERE id = '{id}'"
            self.cursor.execute(query)
            self.conn.commit()
        except connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()

    def getById(self, entity, id):
        try:
            query = f"SELECT * FROM {entity} WHERE id = '{id}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except connector.Error as err:
            print(f"Error: {err}")
            return None
    
    def close (self):
        self.cursor.close()
        self.conn.close()


class LocalStorageAccess(DataAccess):
    def __init__(self):
        self.path = './local_storage/'

    def get(self, entity: str):
        try:
            with open(self.path + entity.lower() + '.json', 'r') as file:
                data = json.load(file)
                return data
        except Exception:
            return []

    def add(self, entity: str, col: List[str], val: List[str]):
        direct = self.path + entity.lower() + '.json'

        if 'id' not in col:
            col = ['id'] + col
            val = [str(uuid.uuid4())] + val

        try:
            data = self.get(entity)
            data.append(dict(zip(col, val)))
            with open(direct, 'w') as file:
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            with open(direct, 'w') as file:
                json.dump([dict(zip(col, val))], file, indent=4)



    def deleteById(self, entity, id):
        direct = self.path + entity.lower() + '.json'
        try:
            with open(direct, 'r') as file:
                data = json.load(file)
            new_data = [item for item in data if item['id'] != id]
            with open(direct, 'w') as file:
                json.dump(new_data, file, indent=4)
        
        except FileNotFoundError:
            print ("No file found!")

    def getById(self, entity, id):
        direct = self.path + entity.lower() + '.json'
        try:
            with open(direct, 'r') as file:
                data = json.load(file)
            enid = [item for item in data if item['id'] == id]
            return enid[0] if enid else None
            
        except FileNotFoundError:
            return None
            
    def close(self):
        pass

class Factory:
    def __init__ (self, data_locate = 'mysql'):
        self.data_locate = data_locate
        
    def createDataAccess(self) -> DataAccess:
        if ( self.data_locate.lower() == 'mysql' 
            or self.data_locate.lower() == 'server'
            or self.data_locate.lower() == 'mysqlserver' 
            or self.data_locate.lower() == 'mysql server'
            or self.data_locate.lower() == 'mysqlserveraccess'
            or self.data_locate.lower() == 'mysql server access'):
            return MySQLServerAccess()
        elif (self.data_locate.lower() == 'local'
                or self.data_locate.lower() == 'localstorage'
                or self.data_locate.lower() == 'local storage'
                or self.data_locate.lower() == 'localstorageaccess'
                or self.data_locate.lower() == 'local storage access'):
            return LocalStorageAccess() 
        return MySQLServerAccess()
        
