from .start import soma

def test_start():
    result_sum = soma(10, 4)

    assert result_sum == 14