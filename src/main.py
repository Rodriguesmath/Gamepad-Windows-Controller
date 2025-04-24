import pygame
import sys
from joystick.connection import conectar_controle, verificar_conexao_controle
from joystick.events import mapear_dpad_para_teclado, mapear_botoes_para_teclado, mapear_botoes_para_mouse, mapear_alt_tab
from joystick.mapping import mover_cursor_com_analogico, mapear_gatilhos_para_volume

pygame.init()
running = True
joystick = conectar_controle()

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
                if event.button == 9:  # Botão B
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