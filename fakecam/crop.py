import cv2

replacement_bg_raw = cv2.imread("tatooine.jpg")
print(replacement_bg_raw.shape)
roi = replacement_bg_raw[60:1020, 320:1600]

cv2.imwrite('new_bg.jpg', roi)
#replacement_bg = cv2.resize(replacement_bg_raw, (width, height))
