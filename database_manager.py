import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def listUserData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT user, pw, email FROM userData").fetchall()
    con.close()
    return data


def listPostData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM postData").fetchall()
    con.close()
    return data


def sortPostData1():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY views DESC LIMIT 1000;"
    ).fetchall()
    con.close()
    return view


def sortPostData2():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY likes DESC LIMIT 1000;"
    ).fetchall()
    con.close()
    return view


def insertContact(user, pw, email):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO userData (user,pw,email) VALUES (?,?,?)", (user, pw, email)
    )
    con.commit()
    con.close()
