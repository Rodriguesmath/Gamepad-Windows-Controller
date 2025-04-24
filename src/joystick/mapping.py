import sys
import os
import pyautogui
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.audio.volume_control import aumentar_volume, diminuir_volume

pyautogui.FAILSAFE = False

def mapear_gatilhos_para_volume(joystick):
    '''
    Traduz as entradas dos eixos do joystick para as funções diminuir e aumentar volume.\n
    @parameters: joystick 
    @return: none
    
    '''
    lt_axis = joystick.get_axis(4)  # LT geralmente no eixo 2
    rt_axis = joystick.get_axis(5)  # RT geralmente no eixo 5

    if lt_axis > 0.5:
        diminuir_volume()

    if rt_axis > 0.5:
        aumentar_volume()
