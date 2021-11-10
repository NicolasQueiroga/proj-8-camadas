
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window


class Signal:
    def __init__(self):
        self.init = 0
        self.DTMF = {
            '1': (679, 1209), '2': (679, 1336), '3': (679, 1477), 'A': (679, 1633),
            '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
            '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
            'X': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
        }
        self.fs = 44100
        self.duration = 2

    def get_fs(self):
        return self.fs

    def get_DTMF(self):
        return self.DTMF

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def print_DTMF(self):
        count = 1
        for k in self.DTMF.keys():
            print(f'{k}', end='')
            if count == 4:
                count = 1
                print()
            else:
                count += 1
                print(' ', end='')

    def generateSin(self, freq, amplitude, time):
        n = self.fs*time
        x = np.linspace(0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal):
        N = len(signal)
        W = window.hamming(N)
        T = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal):
        x, y = self.calcFFT(signal)
        plt.figure('Transformada de Fourier do sinal resultante "G"')
        plt.plot(x, np.abs(y), 'r')
        plt.title('Transformada de Fourier do sinal resultante "G"')
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Re{G}')
        return (x, y)

    def filtro(self, y, samplerate, cutoff_hz):
        nyq_rate = samplerate/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = window.kaiserord(ripple_db, width)
        taps = window.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        yFiltrado = window.lfilter(taps, 1.0, y)
        return yFiltrado

    def LPF(self, signal, cutoff_hz, fs):
            nyq_rate = fs/2
            width = 5.0/nyq_rate
            ripple_db = 60.0 #dB
            N , beta = window.kaiserord(ripple_db, width)
            taps = window.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
            return( window.lfilter(taps, 1.0, signal))