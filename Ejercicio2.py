#Se importa la libreria de CV2
import cv2
#Ruta de la imagen
fileImage = "./itsva.png"
#Imagen en bits
image = cv2.imread(fileImage)
#Se visualiza la imagen original
cv2.imshow("Logo",image)
#Función para convertir imagen a escalas grises
Grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Calculando el umbral del logotipo
valor,umbralImagen = cv2.threshold(Grises, 127, 255, 0)
#Introduciendo los contornos en la imagen
contImage,_ = cv2.findContours(umbralImagen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Escribiendo los contornos de la imagen
cv2.drawContours(image, contImage, -1, (0, 255, 0))
#Se visualiza la imagen con bordes
cv2.imshow("Logo con contorno",image)
#Tiempo de espera para cerrar las imagenes
cv2.waitKey(0)