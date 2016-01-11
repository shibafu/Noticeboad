#!/usr/bin/python --
# coding:utf-8

#pythonのインポートファイル　まとめてここに

#外部ドライバやパッケージ
import MySQLdb
import cgi
# enable debugging
import cgitb
cgitb.enable()

#内部ファイル
import Sql_con
import InputForm
import InputBox
import DBoutput


#Html文章の作成
class Html_tagPot:
    def __init__(self):
        self.Html_tagStr =""
    def tagPotin(self, Html_tag):
        self.Html_tagStr = self.Html_tagStr + Html_tag 
    def tagPotout(self):
        return self.Html_tagStr


if __name__ == "__main__":
    #CGI初期設定
    print "Content-Type: text/html\n\n"
    #DB接続
    mainX_Sql = Sql_con.MySQLdbConn()

    #Html文作成
    Ht = Html_tagPot()

    #ヘッダー部分
    Ht.tagPotin( "<html>\n")
    Ht.tagPotin( "  <head>\n")
    Ht.tagPotin( "    <meta http-equiv=\"Content-Type\"")
    Ht.tagPotin("content=\"text/html; charset=utf-8\">\n")
    Ht.tagPotin(    "<script type=\"text/javascript\"\n")
    Ht.tagPotin(    "src=\"./jQueryCore/jquery-2.2.0.js\">\n")
    Ht.tagPotin( "</script>\n")
    Ht.tagPotin("  </head>\n")
  
    #ボディ部分
    Ht.tagPotin("  <body>\n")
    Ht.tagPotin("    <p>タグうちテスト</p>\n")
  
    #DB入力部分
    mainX_InputBox = InputBox.InputBoxCls()

    mainX_InputForm = InputForm.InputFormCls(mainX_Sql)

    SqlQuery = "SELECT * FROM Test;"
    #DB取得
    mainX_Result = mainX_Sql.querySelect(SqlQuery);


    #DBをhtmlに出力

    i = 0

    for x in mainX_Result:
        Ht.tagPotin("<p>" + str(mainX_Result[i][1].encode('utf8'))+"</p>\n")
        i = i + 1
    #ループの増加タイミングで最後のmainx[i]が出力されないため
    #Ht.tagPotin("<p>" + str(mainX_Result[i][1].encode('utf8'))+"</p>\n")

    DBoutput.DBoutputCls.doutput(mainX_Result)

    Ht.tagPotin("  </body>\n")
    Ht.tagPotin("</html>\n")

    print(Ht.tagPotout()) 

    mainX_Sql.close()
