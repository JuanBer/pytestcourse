from mydb import MyDB
import pytest

# Cur method it is passed to each test case as a parameter
# Fixtures leverage a concept of Dependency injection
# No need of global variables
# with the scope module sets up the db once
@pytest.fixture(scope="module")
def curs():
    print("Setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    #after all test cases executer close the connection, instead of ussing return
    yield curs
    curs.close()
    conn.close()
    print("Clossing Connection")

def test_johns_id(curs):
    id = curs.execute("select id from employee_db where name='John'")
    assert id == 123

def test_tom_id(curs):
    id = curs.execute("select id from employee_db where name='Tom'")
    assert id == 789

def test_unexisting_user(curs):
    id = curs.execute("select id from employee_db where name='Peter'")
    assert id == -1