import os
import json
import csv

msg = "What do you want to do?"


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

cars = []

#create class
class Car():
    #create object
    def getCarData(self):
        return self.carMake + " " + self.carYear + " " + self.carColor
    #initialize template (assign values for each variable)
    def __init__(self, make, year, color):
        self.carMake = make
        self.carYear = year
        self.carColor = color

def createCar():
    tempCar = Car(input("What make is your car?\n").capitalize(), input("What year was your car made?\n"), input("What color is your car?\n").capitalize())
    clearConsole()
    #temp.carMake = input("What make is your car?")
    #temp.carYear = input("When was your car made?")
    #temp.carColor = input("What color is your car?")
    return tempCar

def viewList():
    for x in cars:
        print(x.getCarData())

def removeCar():
    viewList()
    carMake = input("What make is your car?\n").capitalize()
    carYear = input("What year is your car?\n")
    carColor = input("What color is your car?\n").capitalize()
    for car in cars:
        if car.carMake == carMake:
            if car.carYear == carYear:
                if car.carColor == carColor:
                    cars.remove(car)
 

def searchCarMake(make):
    for i in cars:
        if i.carMake==make:
            print(i.getCarData())


def searchCarYear(year):
    for i in cars:
        if i.carMake == year:
            print(i.getCarData())


def searchCarColor(color):
    for i in cars:
        if i.carMake == color:
            print(i.getCarData())


def saveToJSON():
    carList = []
    for car in cars:
        dict = {"carType": car.carMake,
            "carYear": car.carYear, "carColor": car.carColor}
        carList.append(dict)
    jsonString = json.dumps(carList, indent=4)
    jsonFile = open('Garage.json', 'a')
    jsonFile.write(jsonString)
    jsonFile.close()

def saveToCsv():
    header = ["carType", "carYear", "carColor"]
    with open("garage.csv", "a") as f:
        writer=csv.writer(f)
        writer.writerow(header)
        for car in cars:
            list = [car.carMake, car.carYear, car.carColor]
            writer.writerow(list)

        

def main():
    global cars
    while(True):
        print(msg)
        print("c - create a car")
        print("v - view current list")
        print("d - delete a car")
        print("em - search for cars by model")
        print("ey - search for cars by year")
        print("ec - search for cars by color")
        print("s - save list to json")
        print("x - exit")
        userChoice = input()
        clearConsole()
        if userChoice == "c":
            cars.append(createCar())
            print("Car added!")
        elif userChoice == "v":
            print("List loaded...")
            viewList()
        elif userChoice == "d":
            removeCar()
            print("Car removed from list!")
        elif userChoice == "s":
            i = input("What file format? Json or CSV?").lower()
            if i == "json":
                saveToJSON()
            elif i == "csv":
                saveToCsv()
        elif userChoice == "em":
            searchCarMake(input("Enter car model: "))
        elif userChoice == "ey":
            searchCarYear(input("Enter car year: "))
        elif userChoice == "ec":
            searchCarColor(input("Enter car color: "))
        elif userChoice == "x":
            return
        else:
            print("Please select an option from the list...")
if __name__ == "__main__":
    main()