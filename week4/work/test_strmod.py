# My test functions
import strmod

def test_concatenation():
  assert "abcdef" == strmod.strmod("+", "abc", "def")
  
def test_replace_easy():
  assert "ale" == strmod.strmod("-", "apple", "pp")

def test_replace_hard():
  assert "ba" == strmod.strmod("-", "banananana", "na")

def test_scramble():
  assert "aaabbb" == strmod.strmod("@", "aba", "bab")
