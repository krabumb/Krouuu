from AnalyseurLexical import *

# get the token list from the functions
# using readFile(filename) to read the file
# generate_token_list(char_list) to get the token list 
# and delete all comments using del_all_comments(token_list)
# the functions are located in file AnalyseurLexical.py
def get_tokens(filename):
    char_list = readFile(filename)
    token_list = generate_token_list(char_list)
    token_list_no_comments = del_all_comments(token_list)
    return token_list_no_comments