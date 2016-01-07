#!/usr/bin/python
#-- coding: utf-8 --

import MySQLdb
#import mysql.connector
class MySQLdbConn:
    def __init__(self):
        self.connection = MySQLdb.connect(host="localhost",
                             port=3306,
                             db="test",
                             user="root",
                             passwd="4980glassland",
                             charset="utf8")

        self.cursor = self.connection.cursor()

#データ出力
    def querySelect(self,query):
        pref_cf = 100
        rowsResult = ""
        #擬似定数
        Final_RecordNum = 40

        #クエリ実行
        self.cursor.execute(query)
        self.connection.commit()

        #Sqlの結果を保存するメンバ変数
        SqlResult = Final_RecordNum*[4*[""]]

        #Sql列代入
        rows = self.cursor.fetchall()
        i = 0
        for row in rows:
            SqlResult[i] = row
            i = i + 1
        #二次元字列を返す　向こうの関数で使うときはstrにキャスト
        return SqlResult

    #SQL代入用関数
    def queryInsert(self,query):
        
        self.cursor.execute(query)
        self.connection.commit()

    #接続終了用関数
    def close(self):
        self.cursor.close()
        self.connection.close()
