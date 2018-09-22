#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Tue Sep 11 16:06:53 2018

#@author: liam

print("This program will determine your primer annealing temperatures")

allowedbases = set('atcgu') # rejects inputs that aren't nucleotide bases
primeredOnce = 1
def tempcalc():
    global primeredOnce
    global primer1temp
    global primer2temp
    global secondgo
    allowedbases = set('atcgu')
    
    while True: #loop for input. Distinguishes input for forward and reverse primer
         if primeredOnce == 1:
              primerin = str(input("Enter the sequence of your first primer\n>>>"))
              primerinlower = primerin.lower()
         elif primeredOnce == 2:
              primerin = str(input("Enter the sequence of your second primer\n>>>"))
              primerinlower = primerin.lower()

         if set(primerinlower).issubset(allowedbases):
              break
         else:
              print("Only valid bases, 'ACTG' can be used. Please try again")

    primera = primerinlower.count('a') #quantifies each base in primer
    primerc = primerinlower.count('c')
    primerg = primerinlower.count('g')
    primert = primerinlower.count('t')

    primertemp = (2*(primera + primert) + 4*(primerc + primerg) - 5) #formula for primer annealing temperature

    if primeredOnce == 1: 
          primer1temp = primertemp
          print("The annealing temperature of your first primer is " + str(primer1temp) +"°C")

    elif primeredOnce == 2:
          primer2temp = primertemp
          print("The annealing temperature of your first primer was " + str(primer1temp) +"°C\nThe annealing temperature of your second primer is " + str(primer2temp) +"°C\n")
          if abs(primer1temp - primer2temp) > 5: #determines how close the temperatures are.
               print("The melting points of your primers are greater than 5°C from each other at " +str(abs(primer1temp - primer2temp)) + "°C difference. It's worth considering different primers.\n")
    if primeredOnce == 1:
          secondgo = input("Would you like to calculate the annealing temperature of a second primer? Press Enter to continue, or 'N' to finish. \n>>>")
    elif primeredOnce == 2:
          secondgo = 'n' #Uses same code for the continue/stop prompt to terminate program after second primer has been calculated
    
    if secondgo.lower() != 'n': #continue stop prompt If n is not entered, counter is increased, and function runs a second time
          primeredOnce = 2
          tempcalc()
    else:
          print("Goodbye!")
if primeredOnce == 1:
     tempcalc()
