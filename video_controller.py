import cv2
vidcap = cv2.VideoCapture('src/music/billie2.mpg')


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        # save frame as JPG file
        cv2.imwrite("src/music/cv2/image"+str(count)+".jpg", image)
    return hasFrames


sec = 0
frameRate = 0.05  # //it will capture image in each 0.5 second
count = 1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
