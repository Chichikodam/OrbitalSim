import math

class Vector():
    def __init__(self, x=0.0, y=0.0,z=0.0): #default values set here rather than when called to make it easier to change default velocity
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): #represent vectors as printable attribute for a programmer
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self): #represent vectors as printable attribute for a user, present in the maths format using i,j,k vectors
        return f"{self.x}i + {self.y}j + {self.x}k"

    def __add__(self, alt): #allows two vector objects to add and produce a new vector from it
        return Vector(self.x + alt.x, self.y + alt.y, self.z + alt.z)

    def __mul__(self, alt):
        if isinstance(alt,(int, float)): #checks whether variable alt is a float or int, not instance of a class
            return Vector(self.x*alt, self.y*alt, self.z*alt)
        else:
            raise ValueError("value must be an integer or float")

    def getSpeed(self): #later on do __getitem__, returns scalar magnitude of all velocity components
        return math.sqrt((self.x**2)+(self.y**2)+(self.z**2))

    def getNormalised(self): #returns normalised vector
        speed = self.getSpeed();
        return Vector(self.x/speed, self.y/speed, self.z/speed)



    def getVal(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise ValueError("Error: You did not enter a valid component number. Must be (0,1,2);")

    def getListVal(self):
        return [self.x, self.y, self.z]



if __name__ == "__main__": #only runs this if called as a main configuration not referenced as directory
    r = Vector(3, 2, 1)
    print(Vector(3,2,1)*2)
    print(repr(Vector(3,2,1)*2))
    print(r.getVal(0))
    print(r.getSpeed())
    print(r.getNormalised())
    print(r.getNormalised().getSpeed())