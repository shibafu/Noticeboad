#!/usr/bin/python
# --coding:utf8--
import logging
import cgi
import cgitb
cgitb.enable()

import SqlAppCore
import Sql_con


class InputFormCls:
    def __init__(self,SqlconnStruct):

        ht1 = SqlAppCore.Html_tagPot()

        form = cgi.FieldStorage()

        #値が入っている時のみ表示する
        if "name" in form and "toukou" in form:
            ht1.tagPotin("<p>Result</p>\n")
            

            #DBにインサート            
            insertQuery = "INSERT INTO Test(Talkid,"
            insertQuery += "Talksentence,"
            insertQuery += "Datetime,"
            insertQuery += "Userid)"

            insertQuery += "VALUES (999999"
            insertQuery += ",\""+ form["toukou"].value + "\""
            insertQuery += ",Date(now())"
            insertQuery +=",999999);"
            SqlconnStruct.queryInsert(insertQuery)
            

            ht1.tagPotin("<p>"+form["name"].value +"</p>\n")
            ht1.tagPotin("<p>"+form["toukou"].value +"</p>\n")

        print(ht1.tagPotout())
