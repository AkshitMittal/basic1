# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:31:15 2020

@author: aks
"""

from flask import Flask, request
app = Flask(__name__)

# The Fibonacci function
def fibo(n: int):
    """
    Calculating the fibonacci numbers
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print("hello")
# The actual route
@app.route("/")
def send_fibo():
    """
    Sending the fibonacci number to the user, telling him if
    he uses improper input
    """
    try:
        return str(fibo(int(request.args['n'])))
    except ValueError:
        return "Please use a number as the 'n' argument"

if __name__ == '__main__':
   app.run()