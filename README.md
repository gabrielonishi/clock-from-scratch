# Arquitetura e Assembler de um Relógio Digital Rodando em FPGA

Esse repositório agrupa o dardware e o assembler utilizado para traduzir um código de relógio digital para FPGA. Feito para a disciplina Design de Computadores, do 6° semestre de Engenharia de Computação do Insper.

## Equipe

 - [Gabriel Hideki Stanzani Onishi](https://github.com/gabrielonishi)
 - [Sarah Azevedo Pimenta da Costa](https://github.com/sarahp31)

## Descrição

O objetivo desse projteto é construir um computador com as funcionalidades básicas de um relógio digital. Para o hardare, utilizou-se o projeto de arquitetura base desenvolvida pelo professor [Paulo Carlos Santos](https://www.escavador.com/sobre/5885956/paulo-carlos-ferreira-dos-santos), desenvolvendo-a em VHDL para o Software Quartus Prime 20.1, da Intel. O software tem influência do [projeto de Assembler do Marco Mello](https://github.com/Insper/DesignComputadores/tree/master/AssemblerASM_BIN_VHDL).

Para mais informações, cheque o [relatório detalhado](https://github.com/gabrielonishi/clock-from-scratch/tree/main/relatorio.pdf).

## Conteúdos

 - `assembler/`: Pasta com o assembler e código assembly.
    - `DOIT.txt`: Loop principal do relógio em assembly.
    - `assembler.py`: Script em python que transforma o assembly em linguagem de máquina (`BIN.txt`).
    - `utils.py`: Encapsulamento de funções utilizadas pelo `assembler.py`.
    - `BIN.txt`: Loop principal do relógio em linguagem de máquina.
 - `hardware/`: Pasta com todos os componentes em VHDL do relógio + arquivos criados pelo Quartus.
 - `relatorio.pdf`: Relatório detalhado das funcionalidades e funcionamento do projeto
