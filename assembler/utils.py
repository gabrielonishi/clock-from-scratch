from typing import Dict

par_mnemonico_codigo = { 
       "NOP":   "0000",
       "LDA":   "0001",
       "SOMA":  "0010",
       "SUB":   "0011",
       "LDI":   "0100",
       "STA":   "0101",
       "JMP":   "0110",
       "JEQ":   "0111",
       "CEQ":   "1000",
       "JSR":   "1001",
       "RET":   "1010",
       "ANDI":  "1011",
       "INC":   "1100",
       "CLT":   "1101",
       "JLT":   "1110"
}

par_registrador_codigo = {
    None:   '00',
    'R0':   '00',
    'R1':   '01',
    'R2':   '10',
    'R3':   '11'
}

def procura_labels(assembly_lines:list) -> dict[str, str]:
    '''
    Vasculha o documento por labels e adiciona
    os endereços em um dicionário

    Argumentos:
     - assembly_lines: lista de linhas do código assembly
    
    Retorna:
     - par_label_linha: dict que associa nome de label com
     sua posição no código
    '''
    par_label_linha: Dict[str, str] = dict()
    numero_de_linha = 0
    
    for line in assembly_lines:
        primeira_letra = line[0]
        if primeira_letra.isalpha():    # Verifica se primeira letra é alguma do alfabeto
            if ':' in line:
                nome_label = line.split(':')[0]
                par_label_linha[nome_label] = numero_de_linha
            numero_de_linha += 1
    
    return par_label_linha

def divide_codigo_de_comentario(assembly_line:str) -> tuple[str, str]:
    '''
    Divide código de comentário
    Nota: Comentário vira toda a linha

    Argumentos:
     - assembly_line: linha de código de assembly
    
    Retorna:
     - code: parte da linha que é de código
     - comment: parte da linha que é comentário
    '''

    splitted_line = assembly_line.split('#')
    code_line = splitted_line[0]
    comment = assembly_line

    # Caso especial para labels
    if ':' in assembly_line:
        code_line = 'NOP'

    return code_line, comment

def identifica_partes_do_codigo(code_line:str) -> tuple[str, str, str]:
    '''
    Divide instrução de argumento

    Argumentos:
     - code_line: parte de código da linha
    
    Retorna:
     - instrucao: instrução da linha
     - registrador: registrador envolvido
     - argumento: imediato, posição de memória ou label

    Exemplo:
     >>> identifica_partes_do_codigo('LDI R0, $0')
     ('LDI', 'R0', '$0')
    '''

    code_line = code_line.replace(',', '')
    splitted_line = code_line.split(' ')
    opcode = splitted_line[0]
    register = None
    argument = None
    for item in splitted_line[1:]:
        if item != '':
            if item in ['R0', 'R1', 'R2', 'R3']:
                register = item
            else:
                argument = item
    return opcode, register, argument

def trata_argumento(instruction:str, argument:str, par_label_linha:dict) -> str:
    '''
    Converte argumento para sua forma binária

    Argumentos:
     - instruction: parte da instrução da linha de código
     - argument: argumento da linha de código
     - par_label_linha: dicionário que associa label com seu número de linha
    
    Retorna:
     - argument_code: argumento na sua forma binária
    '''

    if argument is None:
        return '0'*9

    elif '@' in argument:
        argument = argument.split('@')[1]
        if instruction in ['JMP', 'JSR', 'JLT', 'JEQ']:
            argument = par_label_linha[argument]

    elif '$' in argument:
        argument = argument.split('$')[1]

    argument_int = int(argument)
    argument_bin = bin(argument_int)[2:]
    argument_str = str(argument_bin)
    argument_code = argument_str.zfill(9)

    return argument_code
