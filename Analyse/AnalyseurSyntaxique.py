from AnalyseurLexical import *

def get_tokens(filename):
    char_list = readFile(filename)
    token_list = generate_token_list(char_list)
    token_list_no_comments = del_all_comments(token_list)
    return token_list_no_comments

tokens = get_tokens('code.krouuu')
current_tokken = tokens.pop(0)

def next() -> Token:
    tokens.pop(0)

def analyserProgramme():
    pass