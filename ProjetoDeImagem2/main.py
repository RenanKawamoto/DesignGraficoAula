from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def inverteHorizontalmente(imagem):
    imagemCriada = []

    for i in range(len(imagem)):
        imagemCriada.append([])
        for j in range(len(imagem[i])):
            imagemCriada[i].insert(0,imagem[i][j])    
    
    return imagemCriada


def rotacionarEm90ParaDireita(imagem):
    imagemCriada = []

    for i in range(len(imagem[0])):
        imagemCriada.append([])
        for j in range(len(imagem)):
            imagemCriada[i].insert(0,imagem[j][i])    
    
    return imagemCriada

def rotacionarEm90ParaEsquerda(imagem):
    imagemCriada = []
    
    for i in range(len(imagem[0])):
        imagemCriada.insert(0, [])
        for j in range(len(imagem)):
            imagemCriada[0].append(imagem[j][i])    
    
    return imagemCriada


img = Image.open("teste2.jpg")

img = np.asarray(img, dtype=np.float32)/255

#img2 = rotacionarEm90ParaEsquerda(img)
img2 = rotacionarEm90ParaDireita(img)

plt.figure(figsize=(5,5))
im = plt.imshow(img2, aspect="equal")
plt.axis("off")
plt.show()


