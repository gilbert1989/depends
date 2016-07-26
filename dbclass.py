import pymysql
import pymongo
import pymysql.cursors
import json
class dbClass:
    def __init__(self,host,user,passwd,db,port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port =port
        self.charset = charset
        self.cursorclass = pymysql.cursors.DictCursor

    def delete(self,sql):
        conn = pymysql.connect(
                        host = self.host , user = self.user, passwd = self.passwd , 
                        db = self.db , port = self.port, charset =self.charset,
                        cursorclass=self.cursorclass)
        cur = conn.cursor()
        sta = cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return sta
    
    def fetchall(self,sql):
        conn = pymysql.connect(host = self.host , user = self.user,
                             passwd = self.passwd , db = self.db , 
                             port = self.port, charset =self.charset,
                             cursorclass=self.cursorclass)
        cur = conn.cursor()
        cur.execute(sql)
        result = []
        for r in cur.fetchall():
            result.append(r)
        conn.close()
        return result
    
class mongodbClass:
    def __init__(self,host,database,table,port =27017):
        self.host = host
        self.port = port
        self.database = database
        self.table =table
    
    def find(self,sql):
        client =pymongo.MongoClient(host=self.host,port=self.port)
        db = client[self.database]
        coll = db[self.table]
        result = []
        for item in coll.find(sql):
            result.append(item)
        return result
    
    def delete(self,sql):
        client =pymongo.MongoClient(host=self.host,port=self.port)
        db = client[self.database]
        coll = db[self.table]
        sta = coll.remove(sql)
        return sta
    
    def insert(self,sql):
        client =pymongo.MongoClient(host=self.host,port=self.port)
        db = client[self.database]
        coll = db[self.table]
        sta = coll.insert(sql)
        return sta
    
    def update(self,sql):
        client =pymongo.MongoClient(host=self.host,port=self.port)
        db = client[self.database]
        coll = db[self.table]
        sta = coll.update(sql)
        return sta
        
if __name__ == "__main__":
    db = mongodbClass("10.10.20.36","goldenservice","customers")
    result =db.find({"tel":"13352211003"})
    print(result)