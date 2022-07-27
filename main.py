import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('./images/image1.jpg')
#
# # Resizing an image
# resized = cv2.resize(img, (500,500))
# cv2.imshow('resized', resized)

# Displaying Images
# cv2.imshow("Testinmgs", img)
# cv2.waitKey()
# cv2.destroyAllWindows()



# Converting images from one type to another
# cv2.imwrite("Testing2.png", img)


# converting images to B&W and Negative effects
# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# print(gray, gray.shape)
# negative = 1 - resized
#
# cv2.imshow("Gray", gray)
# cv2.imshow("Negative", negative)
# cv2.waitKey()
# cv2.destroyAllWindows()


# Creating your own images
img = np.zeros((500,500, 3), dtype=np.uint8)
# print(img)


# Changing the color of your image
img[:]= [120, 200,255]




# Writing text on your image
edited = cv2.putText(img, "Hello World", (100,100), cv2.FONT_HERSHEY_DUPLEX ,2, (0,0,0))
# cv2.imshow("Blank", img)
# cv2.imshow("Edited", edited)
# cv2.waitKey()
# cv2.destroyAllWindows()


# Editing image with matplotlib
rgb = cv2.cvtColor(edited, cv2.COLOR_BGR2GRAY)
plt.imshow(rgb)
plt.show()


