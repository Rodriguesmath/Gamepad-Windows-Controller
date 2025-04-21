def aumentar_volume(pulse):
    sink = pulse.sink_list()[0]
    current_volume = sink.volume.value_flat
    new_volume = min(current_volume + 0.05, 1.5)
    pulse.volume_set_all_chans(sink, new_volume)
    print(f"Volume aumentado para: {new_volume * 100:.1f}%")


def diminuir_volume(pulse):
    sink = pulse.sink_list()[0]
    current_volume = sink.volume.value_flat
    new_volume = max(current_volume - 0.05, 0.0)
    pulse.volume_set_all_chans(sink, new_volume)
    print(f"Volume diminuído para: {new_volume * 100:.1f}%")