#!/usr/bin/env python3

import requests

api_base = "https://covid-api.mmediagroup.fr/v1"

def menu():
  print("Welcome to covid-19 search:\nPlease choose one of the following options:\n")
  choice = input("1: Search Cases\n2: History\n3: Vaccines\n<Anything else> Cancel and quit\n")
  switch = { "1": option_cases }
  case =  switch.get(choice, default)
  case()

def option_cases():
  choice = input("To continue, please, choose a search method:\n1: COUNTRY NAME(i.e. France)\n2: COUNTRY ABREVIATION(i.e. FR)\n3: CONTINENT(i.e. Europe)\n<Anything else>: Drop and quit\n")
  endpoint = "/cases"
  info = ""
  switch = {"1": input, "2": input, "3": input}
  case = switch.get(choice, default)
  if choice == "1":
    info = case("Input a country name:\n")
    response = requests.get(api_base+endpoint, params={ "country": info })
    if not response.ok:
      print("Failed requests, status code: {}".format(response.status_code))
      option_cases()
    print(response.json())
  elif choice =="2":
    info = case("Input a country abreviation:\n")
    response = requests.get(api_base+endpoint, params={ "ab": info })
    if not response.ok:
      print("Failed requests, status code: {}".format(response.status_code))
      option_cases()
    print(response.json())
  elif choice =="3":
    info = case("Input a continent name:\n")
    response = requests.get(api_base+endpoint, params={ "continent": info })
    if not response.ok:
      print("Failed requests, status code: {}".format(response.status_code))
      option_cases()
    print(response.json())
  else:
    case()
  
def default():
  print("Canceling and quitting.\nGood-bye :)\n")
  
def main():
  menu()


if __name__ == "__main__":
  main()
