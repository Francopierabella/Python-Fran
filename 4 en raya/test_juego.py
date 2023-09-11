from Juego import Turno
import pytest
def test_Turno():
    assert Turno(2) == 'R'
    assert Turno(1) == 'N'

