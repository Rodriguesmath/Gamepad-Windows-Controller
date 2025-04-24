import pyautogui

def mover_cursor_com_analogico(joystick, sensibilidade=80):                         
    axis_x = joystick.get_axis(2)  # Eixo horizontal do analógico direito
    axis_y = joystick.get_axis(3)  # Eixo vertical do analógico direito

    x, y = pyautogui.position()

    x += int(axis_x * sensibilidade)
    y += int(axis_y * sensibilidade)

    pyautogui.moveTo(x, y)