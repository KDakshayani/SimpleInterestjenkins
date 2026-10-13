from simpleInterest import simInt
def test_simpleInt_pos():
    assert simInt(20000,8,12)==19200

def test_simpleInt_zero():
    assert simInt(0,8,12)==0