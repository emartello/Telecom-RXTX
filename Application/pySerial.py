import serial
import serial.tools.list_ports

def listaPortas():
    portas = list(serial.tools.list_ports.comports())
    for p in portas:
        print(p)

def abrePorta(COMport, baudrate, bytesize, parity, stopbits):     #COMport='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1
    try:
        port = serial.Serial(COMport, baudrate, bytesize, parity, stopbits)
    except serial.SerialException:
       print('Erro ao abrir porta!')
    return port

def transmiteDado(port, valor):
    try:
        port.write(valor)
        port.close
    except:
        print('Dado não enviado!')

def recebeDado(port):
    try:
        valor = porta.read()
        porta.close
    except:
        print('Erro ao receber dado!') 
    return valor

'''listaPortas()

porta1 = abrePorta('COM7', 19200, 8, 'N', 1)
porta2 = abrePorta('COM6', 19200, 8, 'N', 1)
transmiteDado(porta1, b'Teqs')
transmiteDado(porta1, b'A')
dado = porta2.read()
print(dado)
dado = porta2.read()
print(dado)'''