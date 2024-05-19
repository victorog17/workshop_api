import time

def dobra_um_numero(numero):
    return numero * 2

def ler_ultimo_numero():
    try:
        with open('numero.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                return int(lines[-1].strip())
            else:
                print("Arquivo está vazio")
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

if __name__ == "__main__":
    while True:
        num = ler_ultimo_numero()
        if num is not None:
            resultado = dobra_um_numero(num)
            print(f"O dobro do número {num} é {resultado}")
            time.sleep(1)
