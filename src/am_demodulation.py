from suaBibSignal import Signal
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import math


audio, samplerate = sf.read("audios/modulado.wav")

s = Signal()
fs = s.get_fs()
T = s.get_duration()
fp = 14e3
sd.default.samplerate = samplerate
sd.default.channels = 1

samples = len(audio)
t = np.linspace(0, samples/samplerate, samples)
portadora = np.cos(2*np.pi*fp*t)

demodulado = audio*portadora

plt.figure('Sinal Demodulado')
plt.plot(t, demodulado)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Sinal Demodulado')

s.plotFFT(demodulado, title='FFT Demodulado')

filtrado = s.filtro(demodulado, samplerate, 4000)

max_val = max(filtrado)
norm_audio = [s/max_val for s in filtrado]

sd.play(norm_audio, fs)
sd.wait()


plt.show()