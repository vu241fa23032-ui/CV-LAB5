import numpy as np
import cv2
import matplotlib.pyplot as plt

def show(img,slicing_wo_bg,slicing_w_bg):
  plt.figure(figsize=(12,10))

  plt.subplot(2,2,1)
  plt.imshow(img,cmap="gray")
  plt.title("Original")

  plt.subplot(2,2,2)
  plt.imshow(slicing_wo_bg,cmap="gray")
  plt.title("Without Background")

  plt.subplot(2,2,3)
  plt.imshow(slicing_w_bg,cmap="gray")
  plt.title("With Background")
  plt.show()


r_min, r_max = 100, 200
img=cv2.imread("/content/drive/MyDrive/womancat.webp",0)
if img is  None:
  print("Image not found")
else:
  slicing_wo_bg=np.zeros(img.shape)
  slicing_w_bg=img.copy()
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      pixel_val=img[i][j]
      if r_min<=pixel_val<=r_max:
        slicing_wo_bg[i,j]=255
        slicing_w_bg[i,j]=255
show(img,slicing_wo_bg,slicing_w_bg)