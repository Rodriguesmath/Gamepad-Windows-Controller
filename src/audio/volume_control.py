from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

def aumentar_volume():
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    novo_volume = min(current + 0.05, 1.0)
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume aumentado para: {novo_volume * 100:.1f}%")

def diminuir_volume():
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    novo_volume = max(current - 0.05, 0.0)
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume diminuído para: {novo_volume * 100:.1f}%")
