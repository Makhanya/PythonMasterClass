
class Train:
    def __init__(self, num):
        self.num_cars = num

    def __repr__(self):
        return "{} car train".format(self.num_cars)
    def __len__(self):
        return (self.num_cars)

a_train = Train(4)
print(a_train)  # 4 car train
print(len(a_train))  # 4