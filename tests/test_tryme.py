from collatz_problem.lib import try_me

def test_tryme():
    assert try_me(3) == [10, 5, 16, 8, 4, 2, 1]
    assert try_me('string') == 'Sorry, your input was invalid! Please use an integer number!'