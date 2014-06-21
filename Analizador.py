import string


# los comentarios para este lenguaje serán --
# solo serán de una línea 

ar_ops = {'+','-','*','/','='}
lo_ops = {'<','>','!'}
interruptions = ar_ops.union(lo_ops).union(' ')


symbols = {'$','_','@'}
chars = symbols.union(string.digits + string.ascii_letters)

# se remueven los comentarios encontrados 
def scan(program):

    # se remueven los comentarios de una línea
    ocurrences = program.find('--')
    counter = ocurrences
    
    while (ocurrences != -1):
        
        while(program[counter] != '\n'):
            counter += 1
            
        program = program[:ocurrences] + program[counter+1:]
        ocurrences = program.find('--')
        counter = ocurrences
    #################################################
    
    # se compactan los espacios en blanco (' ', \t y \n))
    program = (program.replace('\n',' ')).replace('\t',' ')
    
    ocurrences = program.find(' ')
    counter = ocurrences
    
    while (ocurrences != -1):
        
        while((program[counter] == ' ')):
            counter += 1
            
        program = program[:ocurrences] + program[counter:]
        ocurrences = program.find(' ')
        counter = ocurrences
    ###################################################
###########################################################


# reconocimiento de tokens
def analysis(program):
    
    lexemeBegin = 0
    lookAhead = 0
    
    while(lookAhead < len(program)):
        pass
##########################


# Simulación autómata que acepta la cadena si_
def recognizingSi_(state, string, index):
    
    if ((state == 0) and (string[index] == 's')):
        recognizingSi_(1, string, index+1)
    elif ((state == 1) and (string[index] == 'i')):
        recognizingSi_(2, string, index+1)
    elif ((state == 2) and (string[index] == '_')):
        recognizingSi_(3, string, index+1)
    elif ((state == 3) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
###############################################


# Simulación autómata que acepta la cadena o_sino
def recognizingO_sino(state, string, index):
    
    if ((state == 0) and (string[index] == 'o')):
        recognizingO_sino(1, string, index+1)
    elif ((state == 1) and (string[index] == '_')):
        recognizingO_sino(2, string, index+1)
    elif ((state == 2) and (string[index] == 's')):
        recognizingO_sino(3, string, index+1)
    elif ((state == 3) and (string[index] == 'i')):
        recognizingO_sino(4, string, index+1)
    elif ((state == 4) and (string[index] == 'n')):
        recognizingO_sino(5, string, index+1)
    elif ((state == 5) and (string[index] == 'o')):
        recognizingO_sino(6, string, index+1)
    elif ((state == 6) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
#################################################


# Simulación autómata que acepta la cadena sino
def recognizingSino(state, string, index):
    
    if ((state == 0) and (string[index] == 's')):
        recognizingSino(1, string, index+1)
    elif ((state == 1) and (string[index] == 'i')):
        recognizingSino(2, string, index+1)
    elif ((state == 2) and (string[index] == 'n')):
        recognizingSino(3, string, index+1)
    elif ((state == 3) and (string[index] == 'o')):
        recognizingSino(4, string, index+1)
    elif ((state == 4) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
###############################################


# Simulción autómata que acepta la cadena mientras
def recognizingMientras(state, string, index):
    
    if ((state == 0) and (string[index] == 'm')):
        recognizingMientras(1, string, index+1)
    elif ((state == 1) and (string[index] == 'i')):
        recognizingMientras(2, string, index+1)
    elif ((state == 2) and (string[index] == 'e')):
        recognizingMientras(3, string, index+1)
    elif ((state == 3) and (string[index] == 'n')):
        recognizingMientras(4, string, index+1)
    elif ((state == 4) and (string[index] == 't')):
        recognizingMientras(5, string, index+1)
    elif ((state == 5) and (string[index] == 'r')):
        recognizingMientras(6, string, index+1)
    elif ((state == 6) and (string[index] == 'a')):
        recognizingMientras(7, string, index+1)
    elif ((state == 7) and (string[index] == 's')):
        recognizingMientras(8, string, index+1)
    elif ((state == 8) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
##################################################


# Simulación autómata que acepta la cadena para
def recognizingPara(state, string, index):
    
    if ((state == 0) and (string[index] == 'p')):
        recognizingPara(1, string, index+1)
    elif ((state == 1) and (string[index] == 'a')):
        recognizingPara(2, string, index+1)
    elif ((state == 2) and (string[index] == 'r')):
        recognizingPara(3, string, index+1)
    elif ((state == 3) and (string[index] == 'a')):
        recognizingPara(4, string, index+1)
    elif ((state == 4) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
###############################################


# Simulación autómata que acepta la cadena entonces
def recognizingEntonces(state, string, index):
    
    if ((state == 0) and (string[index] == 'e')):
        recognizingEntonces(1, string, index+1)
    elif ((state == 1) and (string[index] == 'n')):
        recognizingEntonces(2, string, index+1)
    elif ((state == 2) and (string[index] == 't')):
        recognizingEntonces(3, string, index+1)
    elif ((state == 3) and (string[index] == 'o')):
        recognizingEntonces(4, string, index+1)
    elif ((state == 4) and (string[index] == 'n')):
        recognizingEntonces(5, string, index+1)
    elif ((state == 5) and (string[index] == 'c')):
        recognizingEntonces(6, string, index+1)
    elif ((state == 6) and (string[index] == 'e')):
        recognizingEntonces(6, string, index+1)
    elif ((state == 7) and (string[index] == 's')):
        recognizingEntonces(8, string, index+1)
    elif ((state == 8) and (string[index] in interruptions)):
        return index-1
    else:
        return -1
###################################################


# Simulación autómata que acepta cadenas del tipo
# [@|$|_]?[a-Z]+([@|$|_]|[a-Z]|[0-9])*
def recognizingID(state, string, index):
    
    if ((state == 0) and (string[index] in symbols)):
        recognizingID(1, string, index+1)
    elif ((state == 0) and (string[index] in string.ascii_letters)):
        recognizingID(2, string, index+1)
    elif ((state == 1) and (string[index] in string.ascii_letters)):
        recognizingID(2, string, index+1)
    elif ((state == 2) and (string[index] in chars)):
        recognizingID(2, string, index+1)
    elif ((state == 2) and (string in interruptions)):
        return index-1
    else:
        return -1
######################################