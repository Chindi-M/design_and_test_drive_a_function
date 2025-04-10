def includes_todo(string):
    if not isinstance(string, str):
        return False
    elif string.find('#TODO') == -1:
        return False
    else:
        print(string)
        return True