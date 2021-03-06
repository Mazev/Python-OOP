class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if app_memory<= self.get_memory_left():
            if self.is_on:
                self.apps.append(app)
                self.memory_taken += app_memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def get_memory_left(self):
        return  self.memory - self.memory_taken

    def status(self):
        memory_left = self.memory - self.memory_taken
        return f"Total apps: {len(self.apps)}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
