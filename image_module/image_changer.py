#!/usr/bin/python3

import PIL, os

def option():
    print('Choose one, or more combined, among\n1:rotate\n2:resize\n0:cancel and exit')
    choose = str(input('numbers: '))
    return choose


def main():
  print("i am working")
  option()

if __name__ == "__main__":
    main()




