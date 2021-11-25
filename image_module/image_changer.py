#!/usr/bin/python3

from PIL import Image
import os

main_path = os.getcwd()
def option():
    print('Choose one option\n1:rotate\n2:resize\n0:cancel and exit')
    choose = str(input('numbers: '))
    if choose == '1':
        x = int(input('Please insert a angle to rotate anti-clockwise\n'))
        print('Starting to rotate by ', x, ' degrees')
        new_rotat(x)
def new_rotat(a):
    images = os.listdir(main_path+'/images')
    image_dir = main_path + '/images/'
    new_image_dir = main_path + '/changed_images/'
    for image in images:
        try:
            Image.open(image_dir+ image).rotate(a).convert('RGB').save(new_image_dir+image)
            print('Successfully rotation of ', a, ' degrees')
        except:
            print('Could not convet this file')


def main():
  option()

if __name__ == "__main__":
    main()




