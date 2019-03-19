from Cardioid import *

def nothing(x):
    pass

cv2.namedWindow("Cardioid")

cv2.createTrackbar('pnt_num', 'Cardioid', 80, 1000, nothing)
cv2.createTrackbar('factor', 'Cardioid', 1, 256, nothing)
cv2.createTrackbar('change_sped', 'Cardioid', 1, 100, nothing)

factor = 0

while True:
    pnt_num = max(cv2.getTrackbarPos('pnt_num', 'Cardioid'), 1)

    im = draw(300, pnt_num, factor)
    cv2.imshow("Cardioid", im)
    cv2.waitKey(1)

    change = cv2.getTrackbarPos('change_sped', 'Cardioid') / 100

    if abs(factor - cv2.getTrackbarPos('factor', 'Cardioid')) > change:
        change *= -1 * (factor - cv2.getTrackbarPos('factor', 'Cardioid')) / (abs(factor - cv2.getTrackbarPos('factor', 'Cardioid')))
    else:
        factor = cv2.getTrackbarPos('factor', 'Cardioid')
        change = 0

    factor += change
