

class Vector3(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_scaler(cls, a):
        return cls(x=a, y=a, z=a)

    def __add__(self, rhs):
        if isinstance(rhs, self.__class__):
            return Vector3(x=self.x + rhs.x,
                           y=self.y + rhs.y,
                           z=self.z + rhs.z)
        elif isinstance(rhs, (int, float, long)):
            return Vector3(x=self.x + rhs,
                           y=self.y + rhs,
                           z=self.z + rhs)
    __radd__ = __add__

    def __sub__(self, rhs):
        if isinstance(rhs, self.__class__):
            return Vector3(x=self.x - rhs.x,
                           y=self.y - rhs.y,
                           z=self.z - rhs.z)
        elif isinstance(rhs, (int, float, long)):
            return Vector3(x=self.x - rhs,
                           y=self.y - rhs,
                           z=self.z - rhs)

    def __mul__(self, rhs):
        if isinstance(rhs, self.__class__):
            return Vector3(x=self.x * rhs.x,
                           y=self.y * rhs.y,
                           z=self.z * rhs.z)
        elif isinstance(rhs, (int, float, long)):
            return Vector3(x=self.x * rhs,
                           y=self.y * rhs,
                           z=self.z * rhs)

    __rmul__ = __mul__
    
    def __truediv__(self, rhs):
        if isinstance(rhs, self.__class__):
            return Vector3(x=self.x / rhs.x,
                           y=self.y / rhs.y,
                           z=self.z / rhs.z)
        elif isinstance(rhs, (int, float, long)):
            return Vector3(x=self.x / rhs,
                           y=self.y / rhs,
                           z=self.z / rhs)

    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z

    def cross(self, rhs):
        return Vector3(x=self.y * rhs.z - self.z * rhs.y,
                       y=self.z * rhs.x - self.x * rhs.z,
                       z=self.x * rhs.y - self.y * rhs.x)

    def __eq__(self, rhs):
        return (self.x == rhs.x and
                self.y == rhs.y and
                self.z == rhs.z)

    def __ne__(self, rhs):
        return (self.x != rhs.x or
                self.y != rhs.y or
                self.z != rhs.z)

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

    @property
    def magnitude(self):
        return sqrt(self.x * self.x +
                    self.y * self.y +
                    self.z * self.z)

    @property
    def direction(self):
        mag = self.magnitude
        return Vector3(self.x / mag,
                       self.y / mag,
                       self.z / mag)

    @staticmethod
    def _test_class():
        """Simple unit tests for the class"""
        print("Running Vector3 tests")
        unit_vec = Vector3(x=1, y=1, z=1)
        print("Unit vector: {}".format(unit_vec))
        if unit_vec != unit_vec:
            print("Fail -1")
            return
        if (unit_vec == unit_vec) != True:
            print("Fail -2")
            return
        if (unit_vec + unit_vec) != (unit_vec * 2):
            print("Fail -3")
            return
        if (unit_vec - unit_vec).magnitude != 0:
            print("Fail -4")
            return
        if (unit_vec / 1) != (unit_vec / unit_vec):
            print("Fail -5")
            return
        if unit_vec.dot(unit_vec) != 3:
            print("Fail -6")
            return
        twos_vec = 1 + unit_vec
        if twos_vec != Vector3.from_scaler(2):
            print("Fail -7")
            return
        if unit_vec.cross(twos_vec) != Vector3.from_scaler(0):
            print("Fail -8")
            return
        if twos_vec.direction != unit_vec.direction:
            print("Fail -9")
            return
        print("Finished tests")
        return