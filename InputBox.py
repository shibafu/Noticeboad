#!/usr/bin/python
# --coding:utf8--
import logging

import SqlAppCore

class InputBoxCls:
    def __init__(self):

        ht1 = SqlAppCore.Html_tagPot()

        ht1.tagPotin("<p>インプットフォーム</p>\n")
    
        #Sql.pyを起動する。form情報はInputFormで取得
        ht1.tagPotin("<form name = \"Form1\" method=\"POST\" "
                   + "action=\"/cgi-bin/Sql.py\">\n")
    
        ht1.tagPotin("<input type =\"text\" name=\"name\""
                   + " size=\"40\">\n")
        ht1.tagPotin("<p>\n")
        ht1.tagPotin("<textarea name =\"toukou\" rows=\"4\""
                   +" cols=\"40\">\n")

        ht1.tagPotin("</textarea>\n")
        ht1.tagPotin("<p>\n")
        ht1.tagPotin("<input type =\"submit\""
                   + " value=\"送信\"><input type =\"reset\""
                   +" value=\"リセット\">\n")
        ht1.tagPotin("</form>\n")

        print(ht1.tagPotout())
