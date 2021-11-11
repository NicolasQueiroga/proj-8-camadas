import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window


class Signal:
    def __init__(self):
        self.fs = 44100
        self.duration = 2

    def get_fs(self):
        return self.fs

    def set_fs(self, f):
        self.fs = f

    def get_DTMF(self):
        return self.DTMF

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def generateSin(self, freq, amplitude, time, samplerate):
        n = samplerate*time
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

    def plotFFT(self, signal, title=''):
        x, y = self.calcFFT(signal)
        plt.figure(title)
        plt.plot(x, np.abs(y), 'r')
        plt.title('Transformada de Fourier do sinal resultante "G"')
        plt.xlabel('Frequência [Hz]')
        plt.ylabel('Re{G}')
        return (x, y)

    def filtro(self, y, samplerate, cutoff_hz):
        nyq_rate = samplerate/2
        width = 5.0/nyq_rate
        ripple_db = 60.0  # dB
        N, beta = window.kaiserord(ripple_db, width)
        taps = window.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        yFiltrado = window.lfilter(taps, 1.0, y)
        return yFiltrado
