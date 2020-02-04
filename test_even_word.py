from even_word import *
import pytest

# @pytest.mark.skip('Implement your function first!')
def test_even_word():
    assert even_word('aaaa') == 0
    assert even_word('potato') == 2
    assert even_word('aabbbb') == 0
    assert even_word('aaabbbccc') == 3
