import kivy
kivy.require('1.8.0')
import serial
import serial.tools.list_ports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.properties import StringProperty

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

class ImageButton(ButtonBehavior, Image):  

    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
    
class TesteImagem(BoxLayout):  
    minhaImagem = StringProperty("led_off.png")
      
    def __init__(self, **kwargs):
        super(TesteImagem, self).__init__(**kwargs)
        
    def mudaFigura(self):
        self.minhaImagem=  "led_on.png"
    #    porta1 = abrePorta('COM1', 19200, 8, 'N', 1)
    #    transmiteDado(porta1, b'L') #L para ligar o led

    def mudaFigura2(self):
        self.minhaImagem=  "led_off.png" 
    #    porta1 = abrePorta('COM1', 19200, 8, 'N', 1)
    #    transmiteDado(porta1, b'D') #D para desligar o led

class MeuPrograma(App):
   def build(self):
     return TesteImagem() 

if __name__ == '__main__':
    MeuPrograma().run()