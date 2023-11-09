def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = value.lower()
    value2 = value[::-1].lower()
    if value.replace(" ", "") == value2.replace(" ", ""):
        return True
    else:
        return False
