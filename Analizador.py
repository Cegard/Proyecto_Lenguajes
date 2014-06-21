import string

# los comentarios para este lenguaje serán --
# solo serán de una línea 

symbols = {'$','_','@'}
ar_ops = {'+','-','*','/','='}
lo_ops = {'<','>','!'}
interruptions = ar_ops.union(lo_ops).union(' ')

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
        return index
    else:
        return -1
###############################################
  
    