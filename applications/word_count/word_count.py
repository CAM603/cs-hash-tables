ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\',
          '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']


def word_count(s):
    # Initialize dictionary
    a_dict = {}

    # Split the string
    s = s.split()
    # Loop through list
    for word in s:
        # Remove non alphanumeric characters
        word = "".join(i.lower() for i in word if not i in ignore)
        # check if word contains anything valid
        if not word:
            continue
        # If word is in the dictionary
        if word in a_dict.keys():
            a_dict[word] += 1
        else:
            a_dict[word] = 1
    return a_dict


print(word_count('":;,.-+=/\\|[]{}()*^&'))
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
