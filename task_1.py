# -*- coding: utf-8 -*-

import cv2
import numpy

if __name__ == '__main__':
    cv2.namedWindow("out_window")
    cap = cv2.VideoCapture("video/fittin.MP4")

    WIDTH, HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('video/output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (WIDTH, HEIGHT))

    while True:
        flag, img = cap.read()

        low_orange = numpy.array((0, 50, 50), numpy.uint8)
        high_orange = numpy.array((70, 255, 255), numpy.uint8)

        try:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(img_hsv, low_orange, high_orange)

            blue_only = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_blue)
            blue_only = cv2.cvtColor(blue_only, cv2.COLOR_HSV2BGR)

            mask = cv2.cvtColor(mask_blue, cv2.COLOR_GRAY2BGR)
            frame = cv2.add(img, mask)  # negative values become 0 -> black

            out.write(frame)
            cv2.imshow("out_window", frame)

        except:
            cap.release()

        ch = cv2.waitKey(50)
        # to exit, press esc
        if ch == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
