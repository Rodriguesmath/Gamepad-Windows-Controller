import pyautogui

def mapear_dpad_para_teclado(dpad_x, dpad_y):
    '''
    Tradutor de entrada do Dpad (os valores variam de acordo com o controle) para teclado.\n
    @parameters: dpad_x, dpad_y\n
    @return: none
    
    '''
    if dpad_x == 0 and dpad_y == 1:
        pyautogui.press('up')  # Pressiona a tecla "Cima"
    elif dpad_x == 0 and dpad_y == -1:
        pyautogui.press('down')  # Pressiona a tecla "Baixo"
    elif dpad_x == -1 and dpad_y == 0:
        pyautogui.press('left')  # Pressiona a tecla "Esquerda"
    elif dpad_x == 1 and dpad_y == 0:
        pyautogui.press('right')  # Pressiona a tecla "Direita"

def mapear_botoes_para_teclado(button):
    '''
    Tradutor de entrada dos botões(os valores variam de acordo com o controle) do joystick em entradas do teclado.\n
    @parameters: button\n
    @return: none

    '''
    if button == 0:  # Botão A
        pyautogui.press('enter')
    elif button == 1:  # Botão B
        pyautogui.press('esc')  
    elif button == 2:  # Botão X
        pyautogui.press('tab')
    elif button == 3:  # Botão Y
        pyautogui.hotkey('alt', 'tab')  # Simula a combinação Alt + Tab para alternar de janela
    elif button == 6:  # Botão select
        pyautogui.press('space')    
    elif button == 7:  # Botão Start
        pyautogui.press('playpause')
    elif button == 8:  # Botão L
        pyautogui.press('f11')

def mapear_botoes_para_mouse(button):
    '''
    Tradutor de entrada dos botões(os valores variam de acordo com o controle) do joystick em botões do mouse.\n
    @parameters: button\n
    @return: none
    
    '''
    if button == 4:  # Botão LB para clique direito
        pyautogui.rightClick()
    elif button == 5:  # Botão RB
        pyautogui.leftClick()  # RB mapeado para click esquerdo do mouse.

def mapear_alt_tab(button):
    if button == 3:  # Vamos usar o botão Y para "Alt + Tab"
        pyautogui.keyDown('alt')
        pyautogui.press('tab')  # Pressiona a tecla "Tab"
    else:
        pyautogui.keyUp('alt')
        pyautogui.keyUp('tab')