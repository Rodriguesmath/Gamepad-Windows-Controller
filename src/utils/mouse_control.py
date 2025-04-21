def mover_cursor_com_analogico(joystick, sensibilidade=50):
    axis_x = joystick.get_axis(2)  # Eixo horizontal do analógico direito
    axis_y = joystick.get_axis(3)  # Eixo vertical do analógico direito

    # Obtém a posição atual do mouse
    x, y = pyautogui.position()

    # Calcula o novo movimento baseado no valor do eixo e na sensibilidade
    x += int(axis_x * sensibilidade)
    y += int(axis_y * sensibilidade)

    # Move o cursor para a nova posição
    pyautogui.moveTo(x, y)