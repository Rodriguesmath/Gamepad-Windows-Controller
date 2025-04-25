import sys
import os
import pyautogui
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.audio.volume_control import aumentar_volume, diminuir_volume

pyautogui.FAILSAFE = False

def mapear_gatilhos_para_volume(joystick):
    """
    Mapeia os gatilhos de um joystick para controlar o volume.
    Este método utiliza os eixos do joystick para detectar a posição dos gatilhos LT (Left Trigger) 
    e RT (Right Trigger). Se o gatilho LT estiver pressionado além de um limite (0.5), o volume será 
    diminuído. Se o gatilho RT estiver pressionado além de um limite (0.5), o volume será aumentado.
    Parâmetros:
        joystick: Objeto do tipo joystick que fornece acesso aos eixos e botões do controle.
    Dependências:
        - A função `diminuir_volume()` deve estar definida para reduzir o volume.
        - A função `aumentar_volume()` deve estar definida para aumentar o volume.
    """
    
    lt_axis = joystick.get_axis(4)  # LT geralmente no eixo 2
    rt_axis = joystick.get_axis(5)  # RT geralmente no eixo 5

    if lt_axis > 0.5:
        diminuir_volume()

    if rt_axis > 0.5:
        aumentar_volume()
