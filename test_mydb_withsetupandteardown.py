from mydb import MyDB

conn = None
cur = None


def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()


def teardown_module(module):
    cur.close()
    conn.close()


def test_johns_id():
    id = cur.execute("select id from employee_db where name='John'")
    assert id == 123


def test_tom_id():
    id = cur.execute("select id from employee_db where name='Tom'")
    assert id == 789


def test_unexisting_user():
    id = cur.execute("select id from employee_db where name='Peter'")
    assert id == -1
