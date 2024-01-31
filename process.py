# import the necessary packages
import argparse
import cv2
import os

# python process.py -p input -o threshed

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=False,
    help="path to image folder", default="input")
ap.add_argument("-o", "--out", required=False,
    help="Output dir", default="threshed")
args = vars(ap.parse_args())



path = os.getcwd()

def main():
    out = args["out"]
    for image_path in os.listdir(args["path"]):
        full_path = os.path.join(path, args["path"], image_path)
        print(full_path)
        out_path = os.path.join(path, args["out"], image_path)
        image = cv2.imread(full_path, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE);


        #change the C-value to get different tolerances for pencil/pen darkness: lower value = more tolerance
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 4.5)


        #image = cv2.GaussianBlur(image,(5,5),0)
        #a,image = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



        cv2.imwrite(out_path, image)

if __name__ == '__main__':
    main()
        

# show the output image
#cv2.imshow("Image", image)
#cv2.waitKey(0)