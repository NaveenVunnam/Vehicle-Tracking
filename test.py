import matplotlib.pyplot as plt
import cv2
im=plt.imread('./test_images/test5.jpg')
cv2.rectangle(im,(858,401),(964,470),(0,0,255),1)
plt.imshow(im)
plt.show()
#print(im.shape[0])
print(im.shape[1]/(1274-1045))