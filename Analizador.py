# los comentarios para este lenguaje serán --
# solo serán de una línea 

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