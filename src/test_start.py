from .start import soma

def test_start():
    '''
        testing soma
    '''
    result_sum = soma(10, 4)

    assert result_sum == 14