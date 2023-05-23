import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
frecuencia_portadora = 10  # Frecuencia de la portadora en Hz
frecuencia_muestreo = 1000  # Frecuencia de muestreo en Hz
tiempo_simulacion = 1  # Tiempo total de simulación en segundos
amplitud_bit_0 = 0  # Amplitud para el bit 0
amplitud_bit_1 = 1  # Amplitud para el bit 1
bits = [0, 1, 0, 1, 1, 0, 0, 1]  # Secuencia de bits a transmitir

# Generación de la señal modulada ASK
tiempo = np.arange(0, tiempo_simulacion, 1 / frecuencia_muestreo)
señal_modulada = np.zeros(len(tiempo))

for i, bit in enumerate(bits):
    t_inicio = i * (1 / frecuencia_portadora)
    t_fin = (i + 1) * (1 / frecuencia_portadora)
    índices = np.where((tiempo >= t_inicio) & (tiempo < t_fin))
    
    if bit == 0:
        señal_modulada[índices] = amplitud_bit_0
    else:
        señal_modulada[índices] = amplitud_bit_1

# Gráfica de la señal modulada
plt.plot(tiempo, señal_modulada)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Modulación ASK')
plt.grid(True)
plt.show()

#py -m pip install numpy para instalar intancias de python
