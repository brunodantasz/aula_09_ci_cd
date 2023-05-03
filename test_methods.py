import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 6
    b = 9

    output = methods.soma(a, b)

    assert output == 15

def test_subtrair():
    a = 25
    b = 5

    output = methods.subtrair(a, b)

    assert output == 20

def test_multiplicar():
    a = 7
    b = 7

    output = methods.multiplicar(a, b)

    assert output == 49

def test_dividir():
    a = 20
    b = 5

    output = methods.dividir(a, b)

    assert output == 4
