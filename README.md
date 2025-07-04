# Ragexe Address Replacer

Script que se aproveita do breve momento da inicialização do processo (quando a proteção contra escrita ainda não foi habilitada) para alterar valores na memória.

Procedimento:
1. Inicia o processo.
2. Espera a memória iniciar os valores default.
3. Escreve na memória os valores alterados.

## Módulos necessários

- pymem
- pywin32

## Execução

1. Ajustar as variáveis `EXE_PATH`, `IP` e `PORT` conforme desejado.
2. Executar como administrador.
