class HanoiTower:
    def __init__(self, rod = 3):
        self.n = rod
        self.rods = [[]] * 3
        self.rods[0] = [i for i in range(rod, 0, -1)]
        self.rods[1] = []
        self.rods[2] = []

    def move(self, from_rod, to_rod):
        rodN = {"A":0,"B":1,"C":2}
        num = self.rods[rodN[from_rod]].pop()
        self.rods[rodN[to_rod]].append(num)
        print(self)

    def __str__(self, payload = None, rod = None, index = None):
        if rod == None:
            payload = ""
            rod = self.rods
            index = self.n
            # print(index)
            try:
                payload += str(rod[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            payload += "\n"
            index -= 1
            return self.__str__(payload, rod, index)
        
        elif index >= 0:
            try:
                payload += str(rod[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(rod[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            if index != 0:
                payload += "\n"
            index -= 1
            return self.__str__(payload, rod, index)
        
        else:
            return payload
         
def Tower_Of_Hanoi(tower:HanoiTower,n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"move 1 from  {from_rod} to {to_rod}")
        tower.move(from_rod,to_rod)
        return
    Tower_Of_Hanoi(tower,n-1, from_rod, aux_rod, to_rod)
    print(f"move {n} from  {from_rod} to {to_rod}")
    tower.move(from_rod,to_rod)
    Tower_Of_Hanoi(tower,n-1, aux_rod, to_rod, from_rod)
    

n = int(input("Enter Input : "))
tower = HanoiTower(n)
print(tower)
Tower_Of_Hanoi(tower,n, 'A', 'C', 'B')
