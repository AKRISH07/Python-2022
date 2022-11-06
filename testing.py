from fileinput import filename
from operator import mul
from basicmath import div, openfile
def test_div():
    assert div(4,2) == 2

def test_mul():
    assert mul(5*2) == 10

def test_open():
    filename = "filename.txt"
    try:
        openfile(filename)
        raise AssertionError("Exception")
    except:
        raise AssertionError("File not found")



#If false raises exception