#!/usr/bin/python
# --coding:utf8--
import logging
import cgi
import cgitb
cgitb.enable()

import Sql

class InputBoxCls:
    def __init__(self):

        ht1 = Sql.Html_tagPot()

        ht1.tagPotin("<p>インプットフォーム</p>")
    
        #Sql.pyを起動する。form情報はInputFormで取得
        ht1.tagPotin("<form name = \"Form1\" method=\"POST\" "
                   + "action=\"/cgi-bin/Sql.py\">")
    
        ht1.tagPotin("<input type =\"text\" name=\"name\""
                   + "size=\"40\">")
        ht1.tagPotin("<p>")
        ht1.tagPotin("<textarea name =\"toukou\" rows=\"4\""
                   +"cols=\"40\">")

        ht1.tagPotin("</textarea>")
        ht1.tagPotin("<p>")
        ht1.tagPotin("<input type =\"submit\""
                   + " value=\"送信\"><input type =\"reset\""
                   +" value=\"リセット\">")
        ht1.tagPotin("</form>")

        print(ht1.tagPotout())
