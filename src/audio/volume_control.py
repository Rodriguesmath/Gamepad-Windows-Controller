from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def get_volume_interface():
    """
    Retrieves the audio endpoint volume interface for controlling the system's audio volume.

    Returns:
        POINTER(IAudioEndpointVolume): A pointer to the IAudioEndpointVolume interface, 
        which allows manipulation of the system's audio volume.
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

def aumentar_volume():
    """
    Increases the system's master volume by 5%, up to a maximum of 100%.

    This function retrieves the current master volume level using the system's
    audio interface, increments it by 5%, and sets the new volume level. If the
    incremented volume exceeds 100%, it is capped at 100%. The new volume level
    is printed to the console as a percentage.

    Note:
        This function assumes the existence of a `get_volume_interface` function
        that provides access to the system's audio interface.

    Raises:
        Any exceptions raised by the system's audio interface methods.
    """
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    novo_volume = min(current + 0.05, 1.0)
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume aumentado para: {novo_volume * 100:.1f}%")

def diminuir_volume():
    """
    Reduz o volume principal do sistema em 5%, garantindo que o volume não fique abaixo de 0%.

    Obtém o nível de volume atual usando a interface de controle de volume,
    calcula o novo nível reduzindo 5% do volume atual e aplica o novo nível.
    O volume é limitado a um mínimo de 0% para evitar valores negativos.

    Prints:
        Exibe o novo nível de volume em porcentagem no console.
    """
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    novo_volume = max(current - 0.05, 0.0)
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume diminuído para: {novo_volume * 100:.1f}%")
