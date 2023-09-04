from tateti_v3 import *
import pytest

def test_coordValida():
    assert (coordValida(0) == False)
    assert (coordValida(1) == True)
    assert (coordValida(3) == True)
    assert (coordValida(4) == False)

def test_checkFila():
    tablero = [['X','X','X'], \
               ['X','O','O'], \
               [' ',' ',' ']]
    assert (checkFila(0, tablero) == True)
    assert (checkFila(1, tablero) == False)
    assert (checkFila(2, tablero) == False)

def test_checkColumna():
    tablero = [['X','X',' '], \
               ['X','O',' '], \
               ['X','X',' ']]
    assert (checkColumna(0, tablero) == True)
    assert (checkColumna(1, tablero) == False)
    assert (checkColumna(2,tablero) == False)

def test_checkDiag():
    tablero = [['O',' ',' '], \
               [' ','O',' '], \
               [' ',' ','O']]
    assert (checkDiag(tablero) == True)
    tablero = [['O',' ',' '], \
               [' ','O',' '], \
               [' ',' ','X']]
    assert (checkDiag(tablero) == False)
    tablero = [[' ',' ',' '], \
               [' ',' ',' '], \
               [' ',' ',' ']]
    assert (checkDiag(tablero) == False)

def test_checkDiagInv():
    tablero = [[' ',' ','X'], \
               [' ','X',' '], \
               ['X',' ',' ']]
    assert (checkDiagInv(tablero) == True)
    tablero = [[' ',' ','X'], \
               [' ','O',' '], \
               ['O',' ',' ']]
    assert (checkDiagInv(tablero) == False)
    tablero = [[' ',' ',' '], \
               [' ',' ',' '], \
               [' ',' ',' ']]
    assert (checkDiagInv(tablero) == False)
