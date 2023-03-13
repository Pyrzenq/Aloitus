# questions.py tests can be found here
# ------------------------------------

import questions

# Test if conversion to integer works as expected

user_input ='100'

def test_ask_user_integer(monkeypatch): # argumenttina monkeypatch-moduli (venv - pytest - )
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful')

# Test if conversion to float works as expected

# Test an error condition when user adds a unit to a floating point number

# Test conversion to boolean

# Test an error condition

# Change methods to static or class methods and test again