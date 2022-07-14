import cv2
import numpy

def load_image(path_img):
    return cv2.imread(path_img)


def main():
    path_img = "images/IMG_21.jpeg"
    img = load_image(path_img)

    # resize to scale 0.2 (di perkecil) soalnya kalo tidak di resize layarnya tidak cukup
    imgResize = cv2.resize(img, None, fx=0.5, fy=0.5)

    # apply guassian blur on src image
    imgBlur = cv2.GaussianBlur(imgResize,(25,25),cv2.BORDER_DEFAULT)

    cv2.imshow("Hasil", imgBlur)
    cv2.imwrite("hasil/hasil.jpeg", imgBlur)
    
if __name__ == '__main__':
    main()
    cv2.waitKey(0)
    
