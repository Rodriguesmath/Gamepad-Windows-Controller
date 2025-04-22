import ctypes

# Função para aumentar o volume do sistema
def aumentar_volume():
    # Obtém o volume atual
    current_volume = ctypes.c_uint()
    ctypes.windll.winmm.waveOutGetVolume(0, ctypes.byref(current_volume))
    current_volume = current_volume.value & 0xFFFF

    # Calcula o novo volume (incrementa 5%)
    new_volume = min(current_volume + int(0.05 * 0xFFFF), 0xFFFF)

    # Define o novo volume
    ctypes.windll.winmm.waveOutSetVolume(0, new_volume | (new_volume << 16))
    print(f"Volume aumentado para: {new_volume / 0xFFFF * 100:.1f}%")

# Função para diminuir o volume do sistema
def diminuir_volume():
    # Obtém o volume atual
    current_volume = ctypes.c_uint()
    ctypes.windll.winmm.waveOutGetVolume(0, ctypes.byref(current_volume))
    current_volume = current_volume.value & 0xFFFF

    # Calcula o novo volume (decrementa 5%)
    new_volume = max(current_volume - int(0.05 * 0xFFFF), 0)

    # Define o novo volume
    ctypes.windll.winmm.waveOutSetVolume(0, new_volume | (new_volume << 16))
    print(f"Volume diminuído para: {new_volume / 0xFFFF * 100:.1f}%")