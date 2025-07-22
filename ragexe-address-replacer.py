import os
import pymem
import time
import win32process

EXE_PATH = r"C:\Jogos\Ragnarok\Ragexe.exe"
IP = "172.65.XX.XX"
TAADDRESS_ADDR = 0x0143E808
DOMAIN_PTR_ADDR = 0x010C97E8
# Entrada dinâmica da porta
porta_input = input("Digite a porta que deseja redirecionar (ex: 6901): ").strip()
if not porta_input.isdigit():
    print("Porta inválida.")
    exit(1)
PORT = int(porta_input)

# 1- Abre o Rag
h_process, h_thread, pid, tid = win32process.CreateProcess(
    None,
    f"\"{EXE_PATH}\" 1rag1",
    None,
    None,
    False,
    0,
    None,
    os.path.dirname(EXE_PATH),
    win32process.STARTUPINFO()
)
pm = pymem.Pymem(pid)
value = f"{IP}:{PORT}".encode("utf-8").ljust(33, b'\x00')
is_taaddress_overwrited = False
is_domain_overwrited = False

# 2- Espera iniciar os valores default (lt-account-01.gnjoylatam.com:6951 e lt-account-01.gnjoylatam.com:6900).
# 3- Sobrescreve com IP e porta definidos.
while True:
    try:
        taaddress = pm.read_string(TAADDRESS_ADDR)
        if not is_taaddress_overwrited and taaddress == "lt-account-01.gnjoylatam.com:6951":
            print(f"[taaddress] substituindo {taaddress} por {IP}:{PORT}")
            pm.write_bytes(TAADDRESS_ADDR, value, len(value))
            is_taaddress_overwrited = True

        domain_addr = pm.read_uint(DOMAIN_PTR_ADDR)
        domain = pm.read_string(domain_addr)
        if not is_domain_overwrited and domain == "lt-account-01.gnjoylatam.com:6900":
            print(f"[domain] substituindo {domain} por {IP}:{PORT}")
            pm.write_bytes(domain_addr, value, len(value))
            is_domain_overwrited = True

        if is_taaddress_overwrited and is_domain_overwrited:
            print(f"sucesso")
            exit(0)
    except pymem.pymem.exception.MemoryWriteError as e:
        print(f"erro ao sobrescrever: {e}")
        exit(1)
    except Exception as e:
        pass
    time.sleep(0.01)