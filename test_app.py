from app import is_palindrome

def test_palindrome():
    assert is_palindrome("madam")
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")
    assert not is_palindrome("python")