from suaBibSignal import Signal
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf


s = Signal()
fs = s.get_fs()
T = s.get_duration()
fp = 14e3
sd.default.samplerate = fs
sd.default.channels = 1


audio, samplerate = sf.read("audios/audio1.wav")
y_audio = audio[:, 1]
samples = len(y_audio)
t = np.linspace(0, samples/fs, samples)
portadora = np.sin(2*np.pi*fp*t)
