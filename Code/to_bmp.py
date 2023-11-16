import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

import argparse
import os
parser = argparse.ArgumentParser()

parser.add_argument("--path", type=str, default="imgs/target_raw.jpg")
parser.add_argument("--save_path", type=str, default="imgs")
parser.add_argument("--folder", type=int, default=0)
parser.add_argument("--target_width", type=int, default=1920)
parser.add_argument("--target_height", type=int, default=1080)

def main():
    args = parser.parse_args()
    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)
    if args.folder == 0:
        if args.path.split(".")[-1] == "bmp":
            raise Exception("File is already in bmp format")
        try:
            img = cv.imread(args.path)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img = Image.fromarray(img)
            img.resize((args.target_width, args.target_height))
            # replace file extension with .bmp
            img.save(args.save_path + "/" + args.path.split("/")[-1].split(".")[0] + ".bmp")
        except:
            raise Exception("Error with file: " + args.path)
    else:
        # first check if the folder exists
        if not os.path.exists(args.path):
            raise Exception("Folder does not exist")
        # get all the files in the folder
        files = os.listdir(args.path)
        for file in files:
            if file.split(".")[-1] == "bmp":
                print(f'File {file} is already in bmp format. Skipping...')
                continue
            try:
                img = cv.imread(args.path + "/" + file)
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                img = Image.fromarray(img)
                img.resize((args.target_width, args.target_height))
                # replace file extension with .bmp
                img.save(args.save_path + "/" + file.split(".")[0] + ".bmp")
            except:
                print("Error with file: " + file)
                continue
    print("Done!")

if __name__ == "__main__":
    main()