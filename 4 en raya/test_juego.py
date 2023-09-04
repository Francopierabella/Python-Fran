import pytest 
import Juego
def test_Turno():
    assert Juego.Turno(2) == 'R'
    assert Juego.Turno(1) == 'N'

