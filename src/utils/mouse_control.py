import pyautogui
 
def mover_cursor_com_analogico(joystick, sensibilidade=80):                         
    """
    Move o cursor do mouse utilizando o analógico direito de um joystick.

    Este método utiliza os eixos horizontais e verticais do analógico direito
    do joystick para calcular o movimento do cursor do mouse na tela.

    Args:
        joystick: Objeto representando o joystick, que deve possuir o método
                  `get_axis(index)` para acessar os valores dos eixos.
        sensibilidade (int, opcional): Fator de sensibilidade para o movimento
                                       do cursor. Valores maiores resultam em
                                       movimentos mais rápidos. O padrão é 80.

    Dependências:
        - pyautogui: Biblioteca utilizada para manipular o cursor do mouse.

    Notas:
        - O eixo horizontal do analógico direito é acessado pelo índice 2.
        - O eixo vertical do analógico direito é acessado pelo índice 3.
        - A posição atual do cursor é obtida e ajustada com base nos valores
          dos eixos multiplicados pela sensibilidade.

    """
    axis_x = joystick.get_axis(2)  # Eixo horizontal do analógico direito
    axis_y = joystick.get_axis(3)  # Eixo vertical do analógico direito

    x, y = pyautogui.position()

    x += int(axis_x * sensibilidade)
    y += int(axis_y * sensibilidade)

    pyautogui.moveTo(x, y)