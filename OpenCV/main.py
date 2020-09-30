import cv2
                                                            # Mask?

image = cv2.imread("fight_club.jpg", )                     # Downloading image
cv2.imshow("LOOK AT THIS DUDE", image)
b, g, r = cv2.split(image)
cv2.imshow('GREEEEEN IMAGE DUUUDE', g)                       # Showing green image (a)

clone1 = g.copy()
clone2 = g.copy()      # Cloning green image (b)

maximum = g[..., 1].max()
minimum = g[..., 1].min()                       # Finding max and min values of green image (c)

thresh = (maximum - minimum) / 2

dimensions = clone1.shape

height1 = clone1.shape[0]
width1 = clone1.shape[1]

for i in range(0, width1):
    for j in range(0, height1):
        clone1[j, i] = thresh            # Editing pixels values to thresh (d)

height2 = clone2.shape[0]
width2 = clone2.shape[1]

for i in range(0, width2):
    for j in range(0, height2):
        clone1[j, i] = 0

cv2.imshow('WHAT THE FUCK IS THIS DUUUDE', clone1)

cv2.waitKey(0)


