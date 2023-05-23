import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
frecuencia_portadora_0 = 10  # Frecuencia de la portadora para el bit 0 en Hz
frecuencia_portadora_1 = 20  # Frecuencia de la portadora para el bit 1 en Hz
frecuencia_muestreo = 1000  # Frecuencia de muestreo en Hz
tiempo_simulacion = 1  # Tiempo total de simulación en segundos
amplitud = 1  # Amplitud de la señal

bits = [0, 1, 0, 1, 1, 0, 0, 1]  # Secuencia de bits a transmitir

# Generación de la señal modulada FSK
tiempo = np.arange(0, tiempo_simulacion, 1 / frecuencia_muestreo)
señal_modulada = np.zeros(len(tiempo))

for i, bit in enumerate(bits):
    if bit == 0:
        señal_modulada += amplitud * np.sin(2 * np.pi * frecuencia_portadora_0 * tiempo)
    else:
        señal_modulada += amplitud * np.sin(2 * np.pi * frecuencia_portadora_1 * tiempo)

# Gráfica de la señal modulada
plt.plot(tiempo, señal_modulada)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Modulación FSK')
plt.grid(True)
plt.show()
