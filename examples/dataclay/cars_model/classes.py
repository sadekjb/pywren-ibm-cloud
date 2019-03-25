from dataclay import DataClayObject, dclayMethod


class Car(DataClayObject):
    """
    @ClassField model str
    @ClassField speed int
    @ClassField cid int
    """
    @dclayMethod(model='str', speed='int', cid='str')
    def __init__(self, model, speed, cid):
        self.model = model
        self.speed = speed
        self.cid = cid


class Cars(DataClayObject):
    """
    @ClassField cars dict<str, Cars_ns13.classes.Car>
    """
    @dclayMethod()
    def __init__(self):
        self.cars = dict()

    @dclayMethod(new_car="Cars_ns13.classes.Car")
    def add(self, new_car):
        self.cars[new_car.cid] = new_car

    @dclayMethod(car_id="str")
    def get_by_id(self, car_id):
        return self.cars[car_id]

    @dclayMethod(return_="str")
    def get_ids(self):
        result = []
        for car_id in self.cars.keys():
           result.append(car_id)
        return "-".join(result)

    @dclayMethod(return_="str")
    def __str__(self):
        result = ["Cars:"]

        for car in self.cars.values():
            result.append(" - Model: %s, Speed: %d, Car ID: %s" % (car.model, car.speed, car.cid))

        return "\n".join(result)
