import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from playsound import playsound
import time

archivo = str(input('archivo de sonido:' ))

muestreo, sonido = waves.read(archivo)

length = sonido.shape[0] / muestreo
print(f"Segundos = {length}[s]")
print('Frecuencia de muestreo de la Señal Original',muestreo)

#Sonido en bruto
print('dimensiones de matriz: ', np.shape(sonido))
print('datos de sonido: ')
print(sonido)
print('Reproducuiendo su sonido seleccionado')
playsound(archivo)

uncanal = sonido[:,0] 
flotante = sonido[:,0]
    
# rango de observación en segundos
inicia=float(input("Rango de inicio:"))
termina=float(input("Rango de final:"))

# observación en número de muestra
a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = uncanal[a:b]


# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
waves.write('parte01.wav', muestreo, parte)
print('Reproducuiendo su sonido recortado')
playsound('parte01.wav')

#Sonido modificado
muestreo2, modificado = waves.read('parte01.wav')

#Amplificar
amp=parte*4
#Atenuar
ate=parte*.7
#Escalamiento
amplitud = np.max(parte)
m=len(parte)
senalmin=np.min(parte)
senalmax=np.max(parte)
senalrango=np.linspace(senalmin,senalmax,m)
print('Rango de Señal')
print(senalrango)

#Arvhivos txt
np.savetxt("Senal_Bruto.txt",sonido)
np.savetxt("Senal_Rango_Recorte.txt",parte)

#Guardar los nuevos sonidos y reproduccion

print('archivo de Amplificar grabado...')
waves.write('Amplificar.wav', muestreo2, amp)
print('Reproducuiendo su sonido recortado Amplificado')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
playsound('Amplificar.wav')


print('archivo de Atenuar grabado...')
waves.write('Atenuar.wav', muestreo2, parte)
print('Reproducuiendo su sonido recortado Atenuado')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
playsound('Atenuar.wav')


#print('archivo de Escalamiento grabado...')
#waves.write('Escalamiento.wav', muestreo2, parte)
#print('Reproducuiendo su sonido recortado Escalado')
#print('5')
#time.sleep(1)
#print('4')
#time.sleep(1)
#print('3')
#time.sleep(1)
#print('2')
#time.sleep(1)
#print('1')
#time.sleep(1)
#playsound('Escalamiento.wav')

# Gráfica
plt.figure('Gráfica de Señales')
plt.subplot(211)
plt.plot(parte,label='Señal recortada entera')
plt.plot(sonido,label='Señal en bruto')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Señal',loc='left')
plt.legend()


plt.subplot(212)
plt.plot(amp,label='Señal recortada Amplificada')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Señal modificada',loc='left')

plt.subplot(212)
plt.plot(ate,label='Señal recortada Atenuar')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

plt.show()