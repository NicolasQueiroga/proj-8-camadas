from suaBibSignal import Signal
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf


audio, samplerate = sf.read("audios/dua.wav")

s = Signal()
s.set_fs(samplerate)
fs = s.get_fs()
T = s.get_duration()
fp = 14e3
sd.default.samplerate = fs
sd.default.channels = 1

y_audio = audio[:, 1]
samples = len(y_audio)
t = np.linspace(0, samples/fs, samples)
portadora = np.cos(2*np.pi*fp*t)

max_val = max(y_audio)
norm_sound = [s/max_val for s in y_audio]

plt.figure('Sinal Normalizado')
plt.plot(t, norm_sound)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Sinal Normalizado')

sd.play(norm_sound)
sd.wait()

filtrado = s.filtro(norm_sound, fs, 4000)

plt.figure('Sinal Filtrado')
plt.plot(t, filtrado)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Sinal Filtrado')

s.plotFFT(filtrado, title='FFT filtrado')

sd.play(filtrado)
sd.wait()

modulado = (filtrado)*portadora

plt.figure('Sinal Modulado')
plt.plot(t, modulado)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Sinal Modulado')

s.plotFFT(modulado, title='FFT Modulado')

sd.play(modulado)
sd.wait()

sf.write("audios/modulado.wav", modulado, fs)
plt.show()
