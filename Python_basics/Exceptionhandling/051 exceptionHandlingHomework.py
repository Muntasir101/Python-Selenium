'''
Created on May 30, 2018
@author: venkateshwara.d
'''
def exceptionHandling():
    try:
        car = {"make": "bmw", "model": "550i", "year": "2016"}
        print(car["color"])
    except:
        print("Key not found")
    finally:
        print("Please try a different key")

exceptionHandling()
