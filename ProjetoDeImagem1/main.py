from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("teste.jpg")

img = np.asarray(img, dtype=np.float32)/255

img2 = []

for i in range(len(img)-1):
    img2.append([])
    for j in range(len(img[i])-1):
        img2[i].insert(0,img[i][j])

plt.figure(figsize=(5,5))

im = plt.imshow(img2, aspect="auto")
plt.axis("off")
plt.show()


