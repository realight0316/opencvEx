# import cv2
# import numpy as np

# img = cv2.imread('/ch01/cat.bmp')
# cropped_img = img[480: 480 + 100, 640: 640 + 600]


## ---------------------------------------------------------

# Import packages
import cv2
import numpy as np

img = cv2.imread('/test/road.jpg')

img_width = img.shape[1]
img_height = img.shape[0]
print('img_width:{}'.format(img_width))
crop_pos_y = (img_height // 3) *2
print(crop_pos_y)

crop_pt_x = img_height
cv2.imshow("original", img)

# Cropping an image
# 앞에 값이 [height범위, width범위]
cropped_image = img[crop_pos_y:img_height-1, 200:img_width-100]
print(cropped_image.shape)
# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()