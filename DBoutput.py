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

                Ht.tagPotin("$('fieldset[name=FieldNameNum" + str(i) +  "]').hide();\n")

                Ht.tagPotin("$('button[name=ButtonNameNum" +str(i)+"]').click(function(){\n")
                Ht.tagPotin("$('fieldset[name=FieldNameNum" + str(i) +  "]').toggle(500)\n")
                Ht.tagPotin("});\n")      
                Ht.tagPotin("});\n\n")
                i = i + 1

        Ht.tagPotin("</script>\n\n")

        for x in RawSentence:
            if(RawSentence[j][1].encode('utf-8') != ''):
               Ht.tagPotin("<button name = ButtonNameNum" +str(j)+ ">書き込み" +str(j+1)+ "</button>\n<br>\n")

               Ht.tagPotin( "<fieldset name =FieldNameNum" + str(j) +  ">\n")
               Ht.tagPotin("<legend>"+str(RawSentence[j][3].encode('utf-8'))+"</legend>\n")

               Ht.tagPotin("<p>")
               Ht.tagPotin(str(RawSentence[j][1].encode('utf-8')))
               Ht.tagPotin("</p>")

               Ht.tagPotin("</fieldset>\n\n")
        
               j = j + 1

        print(Ht.tagPotout())
