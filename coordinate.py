# importing required packages
import cv2
import numpy as np


# mouse call back function
def click_event(event, x, y,
                flags, params):
    # if the left button of mouse
    # is clicked then this
    # condition executes
    if event == cv2.EVENT_LBUTTONDOWN:

        # appending the points we
        # clicked to list
        points.append((x, y))

        # marking the point with a circle
        # of center at that point and
        # small radius
        cv2.circle(img,(x, y), 4,
                   (0, 255, 0), -1)

        # if length of points list
        # greater than2 then this
        # condition executes
        if len(points) >= 2:
            # joins the current point and
            # the previous point in the
            # list with a line
            cv2.line(img, points[-1], points[-2],
                     (0, 255, 255), 5)

        # displays the image
        cv2.imshow('image', img)



# making an black image
# of size (512,512,3)
# create 3-d numpy
# zeros array
img = np.zeros((512, 512, 3),
               np.uint8)

# declare a list to append all the
# points on the image we clicked
points = []

# show the image
cv2.imshow('image', img)

# setting mouse call back
cv2.setMouseCallback('image',
                     click_event)

# no waiting
cv2.waitKey(0)

# To close the image
# window that we opened
cv2.destroyAllWindows()