import pygame

# TODO: Solve issue with joystick connection


def conectar_controle():
    """
    Connects a joystick controller to the software.
    This utility checks if there is at least one joystick connected. If a joystick is found, it initializes the first joystick and returns its instance. Otherwise, it returns None.
    Returns:
        pygame.joystick.Joystick: An instance of the connected joystick if available.
        None: If no joystick is connected.
    """
    
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick
    else:
        return None


def verificar_conexao_controle(joystick):
    """
    Continuously checks the integrity of the controller connection.
    This method verifies if the joystick is connected and initialized.
    If the controller is disconnected, it reinitializes the joystick subsystem.
    Args:
        joystick (pygame.joystick.Joystick): Instance of the joystick to be checked.
    Returns:
        pygame.joystick.Joystick or None: Returns the joystick instance if it is connected and initialized,
        otherwise, returns None.
    """

    if pygame.joystick.get_count() == 0 or not joystick.get_init():
        print("Controle desconectado. Reinicializando o subsistema de joystick...")
        pygame.joystick.quit()
        pygame.joystick.init()
        return None
    return joystick