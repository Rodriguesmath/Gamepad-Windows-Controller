import pygame

def conectar_controle():

    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick
    else:
        return None


def verificar_conexao_controle(joystick):

    if pygame.joystick.get_count() == 0 or not joystick.get_init():
        print("Controle desconectado. Reinicializando o subsistema de joystick...")
        pygame.joystick.quit()
        pygame.joystick.init()
        return None
    return joystick