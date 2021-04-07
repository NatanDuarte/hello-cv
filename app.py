import cv2 as cv
import numpy as np
import sys, os, urllib.request

# loading the sample image from unsplash random API
req = urllib.request.urlopen(
    'https://source.unsplash.com/random/?korea,asia')

# convert into a cv2 compatible object
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
image = cv.imdecode(arr, -1) # 'Load it as it is'

if image is None:
    sys.exit("Could not find image.")

# resizing the image if it is too big
if image.shape[1] > 800:
    height, width = image.shape[:2]
    # the resized image is three times smaller then the original
    image = cv.resize(
        image,
        (width // 3, height // 3),
        interpolation = cv.INTER_CUBIC
    )

# creating black'n white version
black_white = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# shows up the image
cv.imshow("Original image", image)
cv.imshow("black n white version", black_white)

k = cv.waitKey(0)

def get_filename():
    name = str(input("filename: "))
    name = name.strip()
    name = name.split(" ")
    name = "-".join(name)
    return name

# saves image
if k == ord('s'):
    filename = get_filename()
    if not os.path.exists('output'):
        os.makedirs('output')
    cv.imwrite(f".\\output\\{filename}.jpg", image)
    cv.imwrite(f".\\output\\{filename}_bw.jpg", black_white)

cv.destroyAllWindows()
