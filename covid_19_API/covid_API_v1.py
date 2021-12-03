#!/usr/bin/env python3

import requests

def menu():
  print("Welcome to covid-19 search:\nPlease choose one of the following options:\n")
  choice = input("1: Search Cases\n2: History\n3: Vaccines\n<Anyother> Cancel and quit\n")
  switch = { "1": option_cases }
  case =  switch.get(choice, default)
  case()

def option_cases():
  print("Option Cases :)\n")
def default():
  print("Canceling and quitting.\nGood-bye :)\n")
  
def main():
  menu()


if __name__ == "__main__":
  main()
