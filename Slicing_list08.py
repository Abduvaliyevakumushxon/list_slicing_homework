def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    a=n
    return list1[::-a]
print(main(['a', 'b', 'c', 'd', 'e', 'f'] , -1))