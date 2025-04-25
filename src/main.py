import pygame
"""
This script initializes a gamepad controller using the Pygame library and maps joystick inputs to keyboard, mouse, 
and system actions. It continuously checks for joystick connection and processes events such as button presses, 
D-pad movements, and analog stick movements.

Modules:
- pygame: Used for handling joystick events and initializing the gamepad.
- joystick.connection: Contains functions to connect and verify the joystick connection.
- joystick.events: Maps joystick button and D-pad inputs to keyboard and mouse actions.
- joystick.mapping: Maps joystick triggers to system volume control.
- utils.mouse_control: Handles cursor movement using the joystick's analog stick.

Functions:
- conectar_controle(): Connects to the joystick.
- verificar_conexao_controle(joystick): Verifies if the joystick is still connected.
- mapear_dpad_para_teclado(dpad_x, dpad_y): Maps D-pad movements to keyboard inputs.
- mapear_botoes_para_teclado(button): Maps joystick button presses to keyboard inputs.
- mapear_botoes_para_mouse(button): Maps joystick button presses to mouse actions.
- mapear_alt_tab(button): Maps joystick button presses to Alt+Tab functionality.
- mapear_gatilhos_para_volume(joystick): Maps joystick trigger movements to system volume control.
- mover_cursor_com_analogico(joystick): Moves the cursor using the joystick's analog stick.

Main Loop:
- Continuously checks for joystick connection and reconnects if disconnected.
- Processes joystick events such as button presses, button releases, and D-pad movements.
- Maps joystick inputs to corresponding keyboard, mouse, or system actions.
- Limits the loop to 30 frames per second using Pygame's Clock.

Exit Condition:
- The script exits when the user presses the "B" button (button index 9) or closes the application window.
"""

from joystick.connection import conectar_controle, verificar_conexao_controle
from joystick.events import mapear_dpad_para_teclado, mapear_botoes_para_teclado, mapear_botoes_para_mouse, mapear_alt_tab
from joystick.mapping import mapear_gatilhos_para_volume
from utils.mouse_control import mover_cursor_com_analogico

pygame.init()
running = True
joystick = conectar_controle()
R3 = 9

while running:
    joystick = verificar_conexao_controle(joystick)

    if joystick is None:
        joystick = conectar_controle()

    if joystick:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                mapear_botoes_para_teclado(event.button)
                mapear_botoes_para_mouse(event.button)
                if event.button == R3: 
                    running = False
            elif event.type == pygame.JOYBUTTONUP:
                mapear_alt_tab(event.button)
            elif event.type == pygame.JOYHATMOTION:
                dpad_x, dpad_y = joystick.get_hat(0)
                mapear_dpad_para_teclado(dpad_x, dpad_y)

        # Verifica se o joystick não é None antes de chamar as funções
        mapear_gatilhos_para_volume(joystick)
        mover_cursor_com_analogico(joystick)

    pygame.time.Clock().tick(30)

pygame.quit()           