import pymysql as sql
def ConnectionPooling():
    db=sql.connect(host='localhost',port=3306,user="root",passwd="12345678",db="medassist",cursorclass=sql.cursors.DictCursor)
    cmd=db.cursor()
    return(db,cmd)