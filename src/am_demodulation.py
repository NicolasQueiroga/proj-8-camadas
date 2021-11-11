from suaBibSignal import Signal
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf


audio, samplerate = sf.read("audios/modulado.wav")

s = Signal()
s.set_fs(samplerate)
fs = s.get_fs()
T = s.get_duration()
fp = 14e3
sd.default.samplerate = fs
sd.default.channels = 1

samples = len(audio)
t = np.linspace(0, samples/fs, samples)
portadora = np.cos(2*np.pi*fp*t)

demodulado = audio*portadora

plt.figure('Sinal Demodulado')
plt.plot(t, demodulado)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Sinal Demodulado')

s.plotFFT(demodulado, title='FFT Demodulado')

filtrado = s.filtro(demodulado, fs, 4000)

s.plotFFT(filtrado, title='FFT Demodulado e Filtrado')

sd.play(filtrado, fs)
sd.wait()

plt.show()
