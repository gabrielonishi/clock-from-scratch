import utils

FILENAME_ASSEMBLY = 'ASM.txt'
FILENAME_DESTINO = 'BIN.txt'

with open(FILENAME_ASSEMBLY, "r") as assembly_file:
    assembly_lines = assembly_file.readlines()

linha_lida = 0

par_label_linha = utils.procura_labels(assembly_lines)
with open(FILENAME_DESTINO, "w") as binary_file:
    for line in assembly_lines:
        primeira_letra = line[0]
        if primeira_letra.isalpha():    # Verifica se primeira letra é alguma do alfabeto
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            code_line, comment = utils.divide_codigo_de_comentario(line)
            instruction, register, argument = utils.identifica_partes_do_codigo(code_line)

            opcode = utils.par_mnemonico_codigo[instruction]
            register_code = utils.par_registrador_codigo[register]
            argument_code = utils.trata_argumento(instruction, argument, par_label_linha)

            bin_line = opcode + register_code + argument_code

            vhdl_line = ('tmp(' + str(linha_lida) + ') := "' +
                        opcode + register_code + argument_code +
                        '";\t-- ' + comment + '\n')
            
            linha_lida += 1
            
            print(vhdl_line, len(bin_line))

            binary_file.write(vhdl_line)
        
        elif primeira_letra == '#':
            binary_file.write('-- ' + line)
