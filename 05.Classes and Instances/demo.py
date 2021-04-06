class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def robot_instances():
        return Robot.__counter


print(Robot.robot_instances())  # 0
x = Robot()
print(x.robot_instances())  # 1
y = Robot()
print(x.robot_instances())  # 2
print(Robot.robot_instances())  # 2
