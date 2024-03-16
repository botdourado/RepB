#importando a biblioteca
import cv2

imagem = cv2.imread("luffy.jpg")
print("largura em pixels:",end="")
print(imagem.shape[1])
print("Altura em Pixels:",end="")
print(imagem.shape[0])
print("Qtde de canais:",end="")
print(imagem.shape[2])

#mostrando a imagem como função.
cv2.imshow("luffy.jpg",imagem)
cv2.waitKey(0)

imagem = cv2.imread("luffy.jpg")
(b,g,r) = imagem[0,0]
print("O pixel (0,0) tem as seguintes cores: ")
print("Vermelho: ",r,"Verde: ",g,"Azul: ",b,)

for y in range(0,imagem.shape[0]):
    for x in range(0,imagem.shape[1]):
        imagem[y,x]=(255,0,0)
cv2.imshow("imagem modificada",imagem)
cv2.waitKey(0)

imagem = cv2.imread("luffy.jpg")
for y in range(0,imagem.shape[0]):
    for x in range(0,imagem.shape[1]):
        imagem[y,x] = (x%256,y%256,x%256)
cv2.imshow("imagem modificada",imagem)
cv2.waitKey(0)

imagem = cv2.imread("luffy.jpg")   
for y in range(0,imagem.shape[0],1):
    for x in range(0,imagem.shape[1],1):
        imagem[y,x] = (0,(x*y)%256,0)
cv2.imshow("imagem modificada",imagem)
cv2.waitKey(0)

imagem = cv2.imread("luffy.jpg")
for y in range(0,imagem.shape[0],10):
    for x in range(0,imagem.shape[1],10):
        imagem[y:y+5, x:x+5] = (0,2555,255)
cv2.imshow("imagem modificada",imagem)
cv2.waitKey(0)

        









