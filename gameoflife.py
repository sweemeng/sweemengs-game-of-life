import time


world = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]

max_point = 7 # We use a square world to make things easy

class GameOfLife(object):
    def __init__(self, world=world, max_point=max_point, value=1):
        self.world = world
        self.max_point = max_point
        self.value = value

    def to_reproduce(self, x, y):
        if not self.is_alive(x, y):
            neighbor_alive = self.neighbor_alive_count(x, y)
            if neighbor_alive == 3:
                return True
        return False

    def to_kill(self, x, y):
        if self.is_alive(x, y):
            neighbor_alive = self.neighbor_alive_count(x, y)
            if neighbor_alive < 2 or neighbor_alive > 3:
                return True
        return False

    def to_keep(self, x, y):
        if self.is_alive(x, y):
            neighbor_alive = self.neighbor_alive_count(x, y)
            if neighbor_alive >= 2 and neighbor_alive <= 3:
                return True
        return False

    def is_alive(self, x, y):
        pos = self.get_pos(x, y)
        return self.world[pos]

    def neighbor_alive_count(self, x, y):
    
        neighbors = self.get_neighbor(x, y)
        alives = 0
        for i, j in neighbors:
            if self.is_alive(i, j):
                alives = alives + 1
        # Because neighbor comes with self, just for easiness
        if self.is_alive(x, y):
            return alives - 1
        return alives
    
    def get_neighbor(self, x, y):
        #neighbors = [
        #    (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
        #    (x + 1, y),     (x, y),     (x, y + 1),
        #    (x + 1, y - 1), (x, y - 1), (x - 1, y - 1),
        #]
        neighbors = [
            (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1),     (x, y),     (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
        ]
        return neighbors

    def get_pos(self, x, y):
        if x < 0:
            x = max_point
        if x > max_point:
            x = 0
        if y < 0:
            y = max_point
        if y > max_point:
            y = 0
    
        return (x * (max_point+1)) + y

    # I am seriously thinking of having multiple species
    def set_pos(self, x, y):
        pos = self.get_pos(x, y)
        self.world[pos] = self.value

    def set_cells(self, cells):
        for x, y in cells:
            self.set_pos(x, y)

    def unset_pos(self, x, y):
        pos = self.get_pos(x, y)
        self.world[pos] = 0

    def run(self):
        something_happen = False
        operations = []
        for i in range(max_point + 1):
            for j in range(max_point + 1):
                if self.to_keep(i, j):
                    something_happen = True
                    continue
                if self.to_kill(i, j):
                    operations.append((self.unset_pos, i, j))
                    something_happen = True
                    continue
                if self.to_reproduce(i, j):
                    something_happen = True
                    operations.append((self.set_pos, i, j)) 
                    continue
        for func, i, j in operations:
            func(i, j)
        if not something_happen:
            print("weird nothing happen")

    def print_world(self):
        count = 1
        for i in self.world:
              
            if count % 8 == 0:
                print("%s " % i)
            else:
                print("%s " % i, end="")
            count = count + 1
        print(count)
    
    def print_neighbor(self, x, y):
        neighbors = self.get_neighbor(x, y)
        count = 1
        for i, j in neighbors:
            pos = self.get_pos(i, j)
            if count % 3 == 0:
                print("%s " % self.world[pos])
            else:
                print("%s " % self.world[pos], end="")
            count = count + 1
        print(count)

    def everyone_alive(self):
        count = 0
        for i in self.world:
            if i:
                count = count + 1
        if count:
            return True
        return False

    def destroy_world(self):
        for i in range(len(self.world)):
            self.world[i] = 0



def main():
    game = GameOfLife()
    cells = [ (2, 4), (3, 5), (4, 3), (4, 4), (4, 5) ]
    game.set_cells(cells)
    print(cells) 
    while True:
        try:
            game.print_world()
            
            game.run()
            count = 0
            time.sleep(5)
        except KeyboardInterrupt:
            print("Destroy world")        
            break

def debug():
    game = GameOfLife()
    cells = [ (2, 4), (3, 5), (4, 3), (4, 4), (4, 5) ]
    game.set_cells(cells)
    test_cell = (3, 3)
    game.print_neighbor(*test_cell) 
    print("Cell is alive: %s" % game.is_alive(*test_cell))
    print("Neighbor alive: %s" % game.neighbor_alive_count(*test_cell))
    print("Keep cell: %s" % game.to_keep(*test_cell)) 
    print("Make cell: %s" % game.to_reproduce(*test_cell)) 
    print("Kill cell: %s" % game.to_kill(*test_cell)) 
    game.print_world()
    game.run()
    game.print_world()

if __name__ == "__main__":
    main()
    #debug()
