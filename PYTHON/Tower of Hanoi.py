"""
id: CRUNZEX, (KMITL)

Example
Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3
"""

class Tower:
    def __init__(self, disk = 3):
        self.disk = disk
        self.towers = [[]] * 3
        self.towers[0] = [index for index in range(self.disk, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def move(self, src_tower, dst_tower):
        num = self.towers[src_tower].pop()
        self.towers[dst_tower].append(num)
        print(self.output(src_tower, dst_tower, num))

    def output(self, src_tower, dst_tower, num):
        return f"move {num} from  {chr(src_tower + 65)} to {chr(dst_tower + 65)}\n{self}"

    def __str__(self, payload = None, town = None, index = None):
        if town == None:
            payload = ""
            town = self.towers
            index = self.disk
            # print(index)
            try:
                payload += str(town[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(town[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(town[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            payload += "\n"
            index -= 1
            return self.__str__(payload, town, index)
        
        elif index >= 0:
            try:
                payload += str(town[0][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(town[1][index]) + "  " 
            except IndexError:
                payload += "|  "
            try:
                payload += str(town[2][index]) + "  " 
            except IndexError:
                payload += "|"
            
            if index != 0:
                payload += "\n"
            index -= 1
            return self.__str__(payload, town, index)
        
        else:
            return payload

def solve(tower:Tower, n, src_tower, dst_tower, aux_tower):
    if n == 0:
        return
    
    solve(tower, n - 1, src_tower, aux_tower, dst_tower)
    tower.move(src_tower, dst_tower)
    solve(tower, n - 1, aux_tower, dst_tower, src_tower)

if __name__ == "__main__":
    tower = Tower(int((input("Enter Input : "))))
    print(tower)
    solve(tower, tower.disk, 0, 2, 1)