
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instances."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        """Return the current floor when we print the instance"""
        return "Current floor: {}".format(self.current)

    #Some methods
    def up(self):
        
        if self.current == self.top:
            return "We can't keep going"
        else:
            self.current +=1


    def down(self):
        if self.current == self.bottom:
            return "We can't keep going"
        else:
            self.current -= 1

    def go_to(self,floor):
        if self.bottom <=floor <= self.top:
            self.current=floor
        else:
            "Wrong floor!"

elevator = Elevator(-1,10,0)
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1


elevator.go_to(5)
print(elevator)