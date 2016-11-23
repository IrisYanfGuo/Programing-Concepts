class RentalProgram(object):
    def __init__(self):
        self.vehiclelist = [[], [], []]
        self.reserlist = []
        self.rentlist = []


        # initialize
        car1 = Car(4, 2, 0.15, 12345)
        car2 = Car(4, 2, 0.15, 12346)
        car3 = Car(4, 2, 0.15, 12347)
        car4 = Car(4, 2, 0.15, 12348)
        car5 = Car(4, 2, 0.15, 12349)

        van1 = Van(3, 0.2, 67543)
        van2 = Van(3, 0.2, 67544)
        van3 = Van(3, 0.2, 67545)
        van4 = Van(3, 0.2, 67546)
        van5 = Van(3, 0.2, 67547)

        trunk1 = Trunk(5, 6, 0.25, 56789)
        trunk2 = Trunk(5, 6, 0.25, 56780)
        trunk4 = Trunk(5, 6, 0.25, 56788)
        trunk5 = Trunk(5, 6, 0.25, 56787)
        trunk6 = Trunk(5, 6, 0.25, 56786)
        self.add_available(car1)
        self.add_available(car2)
        self.add_available(car3)
        self.add_available(car4)
        self.add_available(car5)
        self.add_available(trunk1)
        self.add_available(trunk2)
        self.add_available(trunk6)
        self.add_available(trunk4)
        self.add_available(trunk5)
        self.add_available(van1)
        self.add_available(van2)
        self.add_available(van3)
        self.add_available(van4)
        self.add_available(van5)



        print("0.check the available vehicle")
        print("1.check the cost")
        print("2.reserve a vehicle")

        num = int(input())
        if num == 0:
           self.listAvali()
        elif num == 1:
            print("please input 1.the type of your car 2: the number of weekdays you are going to rent 3. weekends"
                  "4.how many weeks 5. miles per day approximus")
            [type, weekday, weekend, week, miles_per_day] = [int(input()), int(input()), int(input()),int(input()),int(input())]
            print(self.cost(type, weekday, weekend, week, miles_per_day))
        else:
            print("please input  your 1. name 2.address 3.credit card 4. type")
            [name, address, creditcard, type] = [input(), input(), input(), int(input())]
            if self.checkAvali(type):
                a = self.rent_vehicle(type)
                self.reserve(name, address, creditcard, a.vin)
            else:
                print("not enough vehicles")

    def listAvali(self):
        print("car:" + str(len(self.vehiclelist[0])))
        print("trunk:" +str( len(self.vehiclelist[1])))
        print("van:" + str(len(self.vehiclelist[2])))

    def checkAvali(self, type):
        if (len(self.vehiclelist[type]) > 0):
            return True
        else:
            return False

    def rent_vehicle(self, type):
        if self.checkAvali(type):
            vehi = self.vehiclelist[type].pop()
            return vehi
        else:
            print("not enough vehicles")

    def cost(self, type, weekday, weekend, week, miles_per_day):
        # with 0 stands for can, 1 stands for van,2 stands for truck
        if type == 0:
            return self.car_cost(weekday, weekend, week, miles_per_day)
        elif type == 1:
            return self.van_cost(weekday, weekend, week, miles_per_day)
        elif type == 2:
           return self.truck_cost()

    def car_cost(self, weekday, weekend, week, miles_per_day):
        fee1 = 24.99 * weekday + 45 * weekend + 180 * week
        fee2 = 0
        if (miles_per_day > 100):
            fee2 = (miles_per_day - 100) * 0.15*(weekday+weekend+week*7)
        return fee1 + fee2

    def van_cost(self, weekday, weekend, week, miles_per_day):
        fee1 = 35 * weekday + 55 * weekend + 220 * week
        fee2 = miles_per_day*(weekday+weekend+week*7)*0.2

        return fee1 + fee2

    def truck_cost(self, weekday, weekend, week, miles_per_day):
        fee1 = 34.95 * weekday + 110 * weekend + 425 * week
        fee2 = 0
        if (miles_per_day > 25):
            fee2 = (miles_per_day - 25) * 0.15*(weekday+weekend+week*7)
        return fee1 + fee2

    def reserve(self, customer_name, address, card, vin):
        a = [customer_name, address, card, vin]
        self.reserlist.append(a)
        print("reservation successful, your car Vin is %s",a[3])

    def add_available(self, a):
        self.vehiclelist[a.type].append(a)


class Vehicles(object):
    def __init__(self, miles_per_gallon, vin):
        self.miles_per_gallon = miles_per_gallon
        self.vin = vin

    def __str__(self):
        return ("miles per gallon: " + self.miles_per_gallon + "\n"
                + "vin: " + self.vin + "\n")


class Car(Vehicles):
    def __init__(self, passengers, doors, miles_per_gallon, vin):
        self.type = 0
        super().__init__(miles_per_gallon, vin)
        self.passengers = passengers
        self.doors = doors

    def cost(self):
        pass

    def __str__(self):
        s = "type : car\n"
        s = s + super().__str__()
        s = s + "max number of passengers: " + self.passengers + "\n"
        s = s + "number of doors: " + self.doors + "\n"
        return s


class Trunk(Vehicles):
    def __init__(self, length, rooms, miles_per_gallon, vin):
        super().__init__(miles_per_gallon, vin)
        self.type = 1
        self.length = length
        self.rooms = rooms

    def cost(self):
        pass

    def __str__(self):
        s = "type : trunk\n"
        s = s + super(Vehicles, self).__str__()
        s = s + "length: " + self.length + "\n"
        s = s + "number of rooms: " + self.rooms + "\n"
        return s


class Van(Vehicles):
    def __init__(self, passengers, miles_per_gallon, vin):
        self.type = 2
        super().__init__(miles_per_gallon, vin)
        self.passengers = passengers

    def __str__(self):
        s = "type : van\n"
        s = s + super().__str__()
        s = s + "max number of passengers: " + self.passengers + "\n"
        return s



a = RentalProgram()
print(a.checkAvali(2))
