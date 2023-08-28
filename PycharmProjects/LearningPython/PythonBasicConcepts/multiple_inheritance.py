"""
1.Multiple Inheritance:A class can inherit attributes and methods from more then one class
2.Method Resolution Order(MRO):Search is done first in the current class, then the search
contineous in the parent classes in depth-first, left-right fashion without searching the same class twice
"""

class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")

class JumpCharacter:
    def jump_1level(self):
        print("jump character 1 level")

    def jump_2level(self):
        print("jump character 2 level")

class Pokemon(MoveCharacter,JumpCharacter):
    pass

p1=Pokemon()
p1.move_fwd()
p1.move_bwd()
p1.jump_1level()
p1.jump_2level()

class Mickey(MoveCharacter,JumpCharacter):
    # pass
    def move_bwd(self):#this method will over ride the parent method and
        # prints content of this method instead of content in parent class bcz it searchs first in the
        #current class
        print("pockemon moving")
p2=Mickey()
p2.move_fwd()
p2.jump_1level()
p2.move_bwd()
print(Mickey.mro())#this will print the resolution order in which this resolution prints