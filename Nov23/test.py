class A(object):  # A must be new-style class
    def __init__(self):
        print
        "enter A"
        print
        "leave A"


class B(C):  # A --> C
    def __init__(self):
        print
        "enter B"
        super(B, self).__init__()
        print
        "leave B"
