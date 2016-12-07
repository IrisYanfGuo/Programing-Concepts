import reclass Matrix(object):    def __init__(self, rows, columns):        self.width = columns        self.height = rows        self.data = []        for i in range(rows):            self.data.append([])            for j in range(columns):                self.data[i].append(0)    def setElementAt(self, x, y, value):        self.data[x][y] = value    def getElementAt(self, x, y):        return self.data[x][y]   # def __init__(self, rows, columns):    #    self.width = columns     #   self.height = rows      #  self.data = [[0] * columns] * rows    def __str__(self):        result = []  # convert a string to lists, first create a [], then called join method, this is more efficient(why efficient?        for row in self.data:            for cell in row:                result.append(str(cell))                result.append(" ")            result.append("\n")        string = "".join(result)        return string# test for Matrix class##a = Matrix(3, 4)#a.setElementAt(1, 1, 9)#print(a.getElement(0, 1))#print(a.getElement(1, 0))#print(a.getElement(0, 0))# a.setElementAt(0,1,2)# a.setElementAt(1,2,1)#print(a)class NumberCell():    def __init__(self, x):        self.value = x    def __str__(self):        return str(self.value)class FormulaCell(object):    def __init__(self, expr, sheet):        self._sheet = sheet        self.formula = expr        self.updateValue()    def updateValue(self):        self.value = eval(self.addCalls(self.formula[1:]))    def __str__(self):        self.updateValue()        return str(self.value)        # transforms the formula stored in a cell into python code    # so A1 => self .lookup(’A1’) # A1 + B1 => self .lookup(’A1’) + self .lookup(’B1’)    def addCalls(self, input):        p = re.compile('[A-Z]+[1-9]+')        matches = p.finditer(input)        result = []        prev = 0        for match in matches:            result.append(input[prev:match.start()])            result.append('self.lookup(\'')            result.append(input[match.start():match.end()])            result.append('\')')            prev = match.end()        result.append(input[prev:])        resultString = ''.join(result)        return resultString    # lookup the value of a given cell .    # x = A1, B22, AB33 ...    def lookup(self, x):        p = re.compile('[A-Z]+')        matches = p.match(x)        to = matches.end()        letters = x[:to]        digits = x[to:]        row = int(digits) - 1        col = self.colNameToInt(letters)        cell = self._sheet.matrix.getElementAt(row, col)        return cell.value    def colNameToInt(self, name):        return ord(name[0]) - 65class Sheet(object):    def __init__(self, x, y):        self.rows = x        self.cols = y        self.matrix = Matrix(x, y)        n = 0        for i in range(x):            for j in range(y):                self.matrix.setElementAt(i , j , NumberCell(n))                n = n + 1    def update_value(self, row, col, new_value):        if (new_value.isdigit()):            cell_object = NumberCell(new_value)        else:            cell_object = FormulaCell(new_value, self)        self.matrix.setElementAt(row, col, cell_object)    def __str__(self):        return self.matrix.__str__()# mysheet = Sheet(3, 4)# print(mysheet.__str__())mysheet =Sheet(3,4)print(mysheet)#errorformula = FormulaCell("=A1+B2",mysheet)mysheet.update_value(1,1,"=A1+B2")print(mysheet)