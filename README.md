# Ragexe Address Replacer

Script que se aproveita do breve momento da inicialização do processo (quando a proteção contra escrita ainda não foi habilitada) para alterar valores na memória.

Procedimento:
1. Inicia o processo.
2. Espera a memória iniciar os valores default.
3. Escreve na memória os valores alterados.

OBS: Executar em modo de administrador.

## Módulos necessários

- pymem
- pywin32
