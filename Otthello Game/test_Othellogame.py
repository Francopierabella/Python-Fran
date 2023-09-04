import pytest
import Othellogame
def test_extremo ():
    assert Othellogame.extremo(3,3) == True
    assert Othellogame.extremo(8,0) == False
    assert Othellogame.extremo(-1,8) == False

def test_opuesto():
    assert Othellogame.opuesto ("O") == "X"
    assert Othellogame.opuesto ("X") == "O"
 
def test_sinUltimos3():
    assert Othellogame.sinUltimos3(["hola","holaa"]) == ["ho","hol"]
    assert Othellogame.sinUltimos3(["Franco","Tomás"]) == ["Fran", "Tom"]

def test_LetraNuemro ():
    assert Othellogame.LetraNumero("a") == 1
    assert Othellogame.LetraNumero("b") == 2
    assert Othellogame.LetraNumero("C") == 3
    assert Othellogame.LetraNumero("D") == 4

def test_strTupla():
    assert Othellogame.strTupla ("A5") == (4,0)
    assert Othellogame.strTupla ("D5") == (4,3)
    assert Othellogame.strTupla ("F3") == (2,5)

def test_turno():
    assert Othellogame.turno ("B",2) == "O"
    assert Othellogame.turno ("N",4) == "X"
    assert Othellogame.turno ("B",3) == "X"
    assert Othellogame.turno ("N",3) == "O"

def test_paso ():
    assert Othellogame.paso((4,4),(4,3)) == (0,-1)
    assert Othellogame.paso((6,2),(2,3)) == (-4,1)
    assert Othellogame.paso((1,2),(3,3)) == (2,1)


def test_valida ():
    assert Othellogame.valida ("A5") == True
    assert Othellogame.valida ("K7") == False
    assert Othellogame.valida ("H8") == True

def test_filtro():
    assert Othellogame.filtro ([(1,2),(-1,2),(-1,3),(2,-1)]) == [(1,2)]
    assert Othellogame.filtro ([(3,3),(7,8),(-1,3)]) == [(3,3),(7,8)]

def test_LetraColor ():
    assert Othellogame.letraColor ("N") == "X"
    assert Othellogame.letraColor ("B") == "O"

def test_tablerolleno ():
    assert Othellogame.tableroLleno([ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','X','-','-',],
    ['-','-','-','X','O','X','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ]) == False
    assert Othellogame.tableroLleno ([ 
    ['O','O','O','O','X','X','X','X',],
    ['O','O','O','O','O','O','O','O',],
    ['O','X','X','O','O','O','X','X',],
    ['O','X','X','O','X','X','X','O',],
    ['O','X','X','X','O','X','O','O',],
    ['O','O','X','O','X','X','O','O',],
    ['O','O','X','X','O','X','X','X',],
    ['O','O','X','X','X','O','O','X',]
    ]) == True

def test_contadorDeFichas():
    assert Othellogame.contadorDeFichas([ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','X','-','-',],
    ['-','-','-','X','O','X','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ]) == "X"
    assert Othellogame.contadorDeFichas([ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','O','X','-',],
    ['-','-','-','X','O','O','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ]) == "O"
    assert Othellogame.contadorDeFichas([ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','-','-','-',],
    ['-','-','-','X','O','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ]) == "-"

def test_verificaLados():
    assert Othellogame.verificaLados(1,3,[ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','-','-','-',],
    ['-','-','-','X','O','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ],"X") == [(1,3)]
    assert Othellogame.verificaLados (2,3,[ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','-','-','-',],
    ['-','-','-','X','O','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ],"X") == [(2,3),(3,3)]

def test_verificacond3 ():
    assert Othellogame.verifica_cond3([(1,1)],[ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','O','X','-','-','-',],
    ['-','-','-','X','O','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ],"X") == [(1,1)]

def test_darvuelta ():
    assert Othellogame.darVuelta([(3,3),(4,4)],[ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','X','-','-','-','-',],
    ['-','-','-','O','X','-','-','-',],
    ['-','-','-','X','O','X','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]],"X") == [ 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','X','-','-','-','-',],
    ['-','-','-','X','X','-','-','-',],
    ['-','-','-','X','X','X','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]]