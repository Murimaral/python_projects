#!/usr/bin/python3

from PIL import Image, UnidentifiedImageError
import os

main_path = os.getcwd()

def option():
    ### Displays menu and triggers one of the following functions
    print('Choose one option\n1:rotate\n2:resize\n<anything-else>:cancel and exit')
    choose = str(input('numbers: '))
    if choose == '1':
        x = int(input('Please insert a angle to rotate anti-clockwise\n'))
        print('Starting to rotate by ', x, ' degrees')
        new_rotat(x)
    elif choose == '2':
        heigth = int(input('Choose new heigth:\n'))
        width = int(input('Choose new width:\n'))
        new_size(width, heigth)
    else:
        print('Canceling and exiting. Good-bye! :)\n')

def new_rotat(a):
    ### Rotates anti-clockwise
    images = os.listdir(main_path+'/images')
    image_dir = main_path + '/images/'
    new_image_dir = main_path + '/changed_images/'
    for image in images:
        try:
            Image.open(image_dir+ image).rotate(a).convert('RGB').save(new_image_dir+image)
            print('Successfully rotation of ', a, ' degrees')
        except UnidentifiedImageError:
            print('Could not convet this file')
        except BaseException as e:
            print('An error ocurred ' + type(e).__name__)
        else:
            print('This pic is ready :)')
def new_size(a,b):
    ### Resizes: a = width and b = heigth
    images = os.listdir(main_path+'/images')
    image_dir = main_path + '/images/'
    new_image_dir = main_path + '/changed_images/'
    for image in images:
        try:
            Image.open(image_dir+ image).resize((a,b)).convert('RGB').save(new_image_dir+image)                         
            print('Successfully resizing: ', a, ' width and ', b, ' heigth')                                                   
        except UnidentifiedImageError: 
            print('Could not convet this file')
        except BaseException as e:
            print('An error ocurred ' + type(e).__name__)
        else:
            print('This pic is ready')

def main():
  option()

if __name__ == "__main__":
    main()




