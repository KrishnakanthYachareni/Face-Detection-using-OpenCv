import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg')

thresholdval1 = 50
thresholdval2 = 100

canny = cv2.Canny(pic, thresholdval1, thresholdval2)

cv2.imshow('canny', canny)

cv2.waitKey(0)

cv2.destroyAllWindows()
