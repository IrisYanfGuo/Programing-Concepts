class Temp():
    # use fahrenheit degree
    def __init__(self, temp):
        self.temp = temp

    def __str__(self):
        return "" + str(self.temp) + " degrees Fahrenheit"

    def aboveFreezing(self):
        if self.temp > 32:
            return True
        else:
            return False

    def convertToFaren(self):
        pass

    def convertToCelcius(self):
        pass
    def convertToKelvin(self):
        pass

class Fahren(Temp):
    def aboveFreezing(self):
        if self.temp > 32:
            return True
        else:
            return False

    def convertToFaren(self):
        pass

    def convertToCelcius(self):
        self.temp = (self.temp-32)*5/9

    def convertToKelvin(self):
        self.temp = (self.temp-32)/1.8 +273.15

    def __str__(self):
        return "" + str(self.temp) + " degrees Fahrenheit"

class Celcius(Temp):
    def aboveFreezing(self):
        if self.temp > 0:
            return True
        else:
            return False

    def convertToFaren(self):
        self.temp = self.temp*1.8+32

    def convertToCelcius(self):
        pass

    def convertToKelvin(self):
        self.temp = self.temp+ 273.15

    def __str__(self):
        return "" + str(self.temp) + " degrees Calcius"

class Kelvin(Temp):
    def aboveFreezing(self):
        if self.temp > 273.5:
            return True
        else:
            return False

    def convertToFaren(self):
        self.temp = (self.temp -273.5 )*1.8

    def convertToCelcius(self):
        self.temp = self.temp-273.5

    def convertToKelvin(self):
        pass

    def __str__(self):
        return "" + str(self.temp) + " degrees Kelvin"