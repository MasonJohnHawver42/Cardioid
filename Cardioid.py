import numpy as np
import math
import cv2

def getPoints(radius, num_points, factor, rot=0):
    points = np.zeros((2, num_points, 2))
    points[0, :, 0] = radius * np.cos((np.arange(0, num_points) * ((2 * math.pi) / num_points)) + rot) + radius
    points[0, :, 1] = radius * np.sin((np.arange(0, num_points) * ((2 * math.pi) / num_points)) + rot) + radius

    points[1, :, 0] = radius * np.cos(((((np.arange(0, num_points) * factor) % num_points) + 1) * ((2 * math.pi) / num_points)) + rot) + radius
    points[1, :, 1] = radius * np.sin(((((np.arange(0, num_points) * factor) % num_points) + 1) * ((2 * math.pi) / num_points)) + rot) + radius

    return points


def draw(radius, num_points, factor, rot=0):
    img = np.zeros(((radius * 2) + 1, (radius * 2) + 1, 3)) + 51
    cv2.circle(img, (radius, radius), radius, (255, 255, 255), 1)

    points = getPoints(radius, num_points, factor, rot)
    for i in range(num_points):
        cv2.circle(img, (int(points[0, i, 0]), int(points[0, i, 1])), 4, (255, 255, 255), -1)
        cv2.line(img, (int(points[0, i, 0]), int(points[0, i, 1])), (int(points[1, i, 0]), int(points[1, i, 1])), (255, 255, 255))

    return img.astype(np.uint8)

im = draw(100, 8, 2)
cv2.imshow("", im)
cv2.waitKey(0)