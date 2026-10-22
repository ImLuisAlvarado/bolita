import pytest

from main import calcular_area_triangulo

def test_calcular_area_triangulo():
    actual_result = calcular_area_triangulo(9, 3)
    #Verificación de coincidencia entre el resultado actual y el resultado esperado.
    assert actual_result == pytest.approx(19.5, abs=0.01)