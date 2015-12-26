from sense_hat import SenseHat
from gameoflife import GameOfLife
import time

WHITE = [ 0, 0, 0 ]
RED = [ 255, 0, 0 ]

def main():

    game = GameOfLife()

    sense = SenseHat()
    # cells = [ (2, 4), (3, 5), (4, 3), (4, 4), (4, 5) ]
    cells = [ (2, 4), (2, 5), (1,5 ), (1, 6), (3, 5)]
    game.set_cells(cells)

    while True:
        
        try:
            
            canvas = []
            for i in game.world:
                if not i:
                    canvas.append(WHITE)
                else:
                    canvas.append(RED)
            sense.set_pixels(canvas)
            game.run()
            if not game.everyone_alive():
                sense.clear()
                print("everyone died")
                break
            time.sleep(0.1)
        except:
            sense.clear()
            break

if __name__ == "__main__":
    main()
    
