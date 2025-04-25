import pyautogui

def mapear_dpad_para_teclado(dpad_x, dpad_y):
    """
    Translates D-pad input into keyboard key presses.
    This function maps the directional pad (D-pad) input from a game controller to corresponding keyboard key presses. 
    The D-pad input values vary depending on the controller.
    Parameters:
        dpad_x (int): The horizontal axis value of the D-pad. Expected values are -1 (left), 0 (neutral), or 1 (right).
        dpad_y (int): The vertical axis value of the D-pad. Expected values are -1 (down), 0 (neutral), or 1 (up).
    Returns:
        None
    """
 
    if dpad_x == 0 and dpad_y == 1:
        pyautogui.press('up')  # Pressiona a tecla "Cima"
    elif dpad_x == 0 and dpad_y == -1:
        pyautogui.press('down')  # Pressiona a tecla "Baixo"
    elif dpad_x == -1 and dpad_y == 0:
        pyautogui.press('left')  # Pressiona a tecla "Esquerda"
    elif dpad_x == 1 and dpad_y == 0:
        pyautogui.press('right')  # Pressiona a tecla "Direita"

def mapear_botoes_para_teclado(button):
    """
    Translates joystick button inputs into keyboard inputs.

    This function maps specific joystick button values to corresponding keyboard actions.
    The button values may vary depending on the joystick model, so adjustments might be necessary.

    Parameters:
        button (int): The identifier of the joystick button pressed.

    Returns:
        None

    Behavior:
        - Button A (0): Simulates pressing the 'Enter' key.
        - Button B (1): Simulates pressing the 'Esc' key.
        - Button X (2): Simulates pressing the 'Tab' key.
        - Button Y (3): Simulates the 'Alt + Tab' key combination to switch windows.
        - Button SELECT (6): Simulates pressing the 'Space' key.
        - Button START (7): Simulates pressing the 'Play/Pause' media key.
        - Button L (8): Simulates pressing the 'F11' key to toggle fullscreen mode.
    """
    
    A = 0
    B = 1
    X = 2
    Y = 3
    SELECT = 6
    START = 7
    L = 8

    if button == A:  # Botão A
        pyautogui.press('enter')
    elif button == B:  # Botão B
        pyautogui.press('esc')  
    elif button == X:  # Botão X
        pyautogui.press('tab')
    elif button == Y:  # Botão Y
        pyautogui.hotkey('alt', 'tab')  # Simula a combinação Alt + Tab para alternar de janela
    elif button == SELECT:  # Botão select
        pyautogui.press('space')    
    elif button == START:  # Botão Start
        pyautogui.press('playpause')
    elif button == L:  # Botão L
        pyautogui.press('f11')

def mapear_botoes_para_mouse(button):
    """
    Mapeia os botões do joystick para ações do mouse.
    Este método traduz os botões do joystick em cliques do mouse, permitindo que 
    os botões do controle sejam usados para interagir com a interface gráfica 
    como se fossem botões do mouse. Os valores dos botões podem variar dependendo 
    do modelo do controle, então ajustes podem ser necessários.
    Parâmetros:
    -----------
    button : int
        O identificador do botão do joystick que será mapeado para uma ação do mouse.
    Retorno:
    --------
    None
        Esta função não retorna nenhum valor. Ela executa ações diretamente 
        através da biblioteca pyautogui.
    """
  
    # Aqui você pode mapear os botões do joystick para ações do mouse
    # Os valores dos botões podem variar dependendo do controle, então ajuste conforme necessário
    # Exemplo de mapeamento:
    # LB = 4, RB = 5
    LB = 4
    RB = 5
    if button == LB:  # Botão LB para clique direito
        pyautogui.rightClick()
    elif button == RB:  # Botão RB
        pyautogui.leftClick()  # RB mapeado para click esquerdo do mouse.

def mapear_alt_tab(button):
    if button == 3:  # Vamos usar o botão Y para "Alt + Tab"
        pyautogui.keyDown('alt')
        pyautogui.press('tab')  # Pressiona a tecla "Tab"
    else:
        pyautogui.keyUp('alt')
        pyautogui.keyUp('tab')