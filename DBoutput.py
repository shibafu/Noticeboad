#!/usr/bin/python --
# coding:utf-8

#pythonのインポートファイル　まとめてここに

# enable debugging
import cgitb
cgitb.enable()

#内部ファイル
import SqlAppCore

class DBoutputCls:
#    def __init__(self):

    @classmethod
    def doutput(cls,RawSentence):
        Ht = SqlAppCore.Html_tagPot()

        i = 0
        j = 0

        Ht.tagPotin("<script type=\"text/javascript\">\n\n")

        Raw_loop = RawSentence

        for x in Raw_loop:
            if(Raw_loop[i][1].encode('utf-8') != ''):
                Ht.tagPotin("$(document).ready(function(){\n")

                Ht.tagPotin("$('button[name=ButtonNameNum" +str(i)+"]').click(function(){\n")
                Ht.tagPotin("$('fieldset[name=FieldNameNum" + str(i) +  "]').toggle(1000)\n")
                Ht.tagPotin("});\n")      
                Ht.tagPotin("});\n\n")
                i = i + 1

        Ht.tagPotin("</script>\n\n")

        for x in RawSentence:
            if(RawSentence[j][1].encode('utf-8') != ''):
               Ht.tagPotin("<button name = ButtonNameNum" +str(j)+ ">ボタン</button>\n")

               Ht.tagPotin( "<fieldset name =FieldNameNum" + str(j) +  ">\n")
               Ht.tagPotin("<legend>ユーザー情報</legend>\n")

               Ht.tagPotin("<p>")
               Ht.tagPotin(str(RawSentence[j][1].encode('utf-8')))
               Ht.tagPotin("</p>")

               Ht.tagPotin("</fieldset>\n\n")
        
               j = j + 1

        print(Ht.tagPotout())
