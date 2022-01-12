class Token:
    def __init__(self, type : str, value : str):
        self.type = type
        self.value = value

    def __str__(self):
        return "[" + self.type + "{" + self.value + "}]"

    def __repr__(self):
        return self.__str__()


def readFile(filename):
    with open(filename, 'r') as f:
        return list(f.read())


def get_type_of_char(char : str):
    if char.isalpha() or char == '_':
        return 0
    elif char.isdigit():
        return 1
    elif char.isspace() and char != '\n':
        return 2
    elif char == '\n':
        return 3
    elif char == "'":
        return 4
    elif char == '"':
        return 5
    elif char == '$':
        return 6
    else:
        return 7

def determine_if_token_is_idf_or_builtin(string : str) -> Token:
    if string == "if":
        return Token("BUILTIN", "if")
    elif string == "elif":
        return Token("BUILTIN", "elif")
    elif string == "else":
        return Token("BUILTIN", "else")
    elif string == "while":
        return Token("BUILTIN", "while")
    elif string == "for":
        return Token("BUILTIN", "for")
    elif string == "foreach":
        return Token("BUILTIN", "foreach")
    elif string == "function":
        return Token("BUILTIN", "function")
    elif string == "break":
        return Token("BUILTIN", "break")
    elif string == "return":
        return Token("BUILTIN", "return")
    elif string == "true":
        return Token("BUILTIN", "true")
    elif string == "false":
        return Token("BUILTIN", "false")
    elif string == "null":
        return Token("BUILTIN", "null")
    elif string == "print":
        return Token("BUILTIN", "print")
    else:
        return Token("IDF", string)


def generate_token_list(char_list : list[str]) -> list[Token]:
    token_list = []
    IDF = False
    idf = ""
    NUMBER = False
    number = 0
    STRINGSIMPLE = False
    stringsimple = ""
    STRINGDOUBLE = False
    stringdouble = ""
    COMMENT = False
    comment = ""
    for char in char_list:
        type_of_char = get_type_of_char(char)
        if IDF:
            if type_of_char == 0 or type_of_char == 1:
                idf += char
            elif type_of_char == 2:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
            elif type_of_char == 3:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
            elif type_of_char == 4:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
                STRINGSIMPLE = True
            elif type_of_char == 5:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
                STRINGDOUBLE = True
            elif type_of_char == 6:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
                COMMENT = True
            else:
                IDF = False
                token_list.append(determine_if_token_is_idf_or_builtin(idf))
                idf = ""
                token_list.append(Token("SYMBOL", char))
        elif NUMBER:
            if type_of_char == 0:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
                IDF = True
                idf += char
            elif type_of_char == 1:
                number *= 10
                number += int(char)
            elif type_of_char == 2:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
            elif type_of_char == 3:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
            elif type_of_char == 4:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
                STRINGSIMPLE = True
            elif type_of_char == 5:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
                STRINGDOUBLE = True
            elif type_of_char == 6:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
                COMMENT = True
            else:
                NUMBER = False
                token_list.append(Token("NUMBER", str(number)))
                number = 0
                token_list.append(Token("SYMBOL", char))
        elif STRINGSIMPLE:
            if type_of_char != 4:
                stringsimple += char
            else:
                STRINGSIMPLE = False
                token_list.append(Token("STRING", stringsimple))
                stringsimple = ""
        elif STRINGDOUBLE:
            if type_of_char != 5:
                stringdouble += char
            else:
                STRINGDOUBLE = False
                token_list.append(Token("STRING", stringdouble))
                stringdouble = ""
        elif COMMENT:
            if type_of_char != 3:
                comment += char
            else:
                COMMENT = False
                token_list.append(Token("COMMENT", comment))
                comment = ""
        else:
            if type_of_char == 0:
                IDF = True
                idf += char
            elif type_of_char == 1:
                NUMBER = True
                number += int(char)
            elif type_of_char == 2 or type_of_char == 3:
                pass
            elif type_of_char == 4:
                STRINGSIMPLE = True
            elif type_of_char == 5:
                STRINGDOUBLE = True
            elif type_of_char == 6:
                COMMENT = True
            else:
                token_list.append(Token("SYMBOL", char))
    return token_list


def del_all_comments(token_list : list[Token]) -> list[Token]:
    new_token_list = []
    for token in token_list:
        if token.type == "COMMENT":
            pass
        else:
            new_token_list.append(token)
    return new_token_list


print(del_all_comments(generate_token_list(readFile("code.krouuu"))))

