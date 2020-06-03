def no_dups(s):
    # Split string
    s = s.split()
    # create dictionary using list item as keys
    # this will remove all duplicates
    # convert back to a list
    s = list(dict.fromkeys(s))
    # convert back to string with spacing
    s = " ".join(s)
    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
