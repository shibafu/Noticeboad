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
    HtHd = Html_tagPot()

    #ヘッダー部分
    HtHd.tagPotin( "<html>\n")
    HtHd.tagPotin( "  <head>\n")
    HtHd.tagPotin( "    <meta http-equiv=\"Content-Type\"")
    HtHd.tagPotin(" content=\"text/html; charset=utf-8\">\n")
    HtHd.tagPotin(    "<script type=\"text/javascript\"\n")
    HtHd.tagPotin(    "src=\"./cgi-bin/jQueryCore/jquery-2.2.0.js\" charset=\"UTF-8\">\n")
    HtHd.tagPotin( "</script>\n\n")

    HtHd.tagPotin(    "<script type=\"text/javascript\"\n")
    HtHd.tagPotin(    "src=\"./jQueryCore/jquery-2.2.0.js\" charset=\"UTF-8\">\n")
    HtHd.tagPotin( "</script>\n")

    HtHd.tagPotin("  </head>\n\n")
  
    #ボディ部分
    HtHd.tagPotin("  <body>\n")
  
    print(HtHd.tagPotout())

    #DB入力部分
    mainX_InputBox = InputBox.InputBoxCls()

    mainX_InputForm = InputForm.InputFormCls(mainX_Sql)

    SqlQuery = "SELECT * FROM NoticeSente;"
    #DB取得
    mainX_Result = mainX_Sql.querySelect(SqlQuery);


    #DBをhtmlに出力
               
    #ループの増加タイミングで最後のmainx[i]が出力されないため
    #Ht.tagPotin("<p>" + str(mainX_Result[i][1].encode('utf8'))+"</p>\n")

    DBoutput.DBoutputCls.doutput(mainX_Result)

    HtBd = Html_tagPot()

    HtBd.tagPotin("  </body>\n")
    HtBd.tagPotin("</html>\n")

    print(HtBd.tagPotout()) 

    mainX_Sql.close()
