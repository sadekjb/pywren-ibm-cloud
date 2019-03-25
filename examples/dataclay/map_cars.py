"""
Simple PyWren example using the map method.

In this example the map() method will launch one
map function for each entry in 'iterdata'. Finally
it will print the results for each invocation with
pw.get_all_result()
"""
import pywren_ibm_cloud as pywren
from dataclay.api import init, finish
#used for the import 
init()
#used to be added for the jobrunner method 
from Cars_ns13.classes import Car, Cars

cars = Cars.get_by_alias('masa_cars13')

iterdata = ['1']
print(cars)
#iterdata = cars.get_ids().split('-')
print(iterdata)

finish()

def my_map_function(x):
    car = cars.get_by_id(x)
    return car.speed

def my_reduce_function(results):
    total = 0
    for map_result in results:
        total = total + map_result
    return total / len(results)

pw = pywren.ibm_cf_executor()

#pw.map(my_map_function, iterdata)
#print(pw.get_result())

pw.map_reduce(my_map_function, iterdata, my_reduce_function)
print(pw.get_result())
