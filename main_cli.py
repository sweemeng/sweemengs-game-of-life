from gameoflife import GameOfLife
import time

def main():

    game = GameOfLife()

    # cells = [ (2, 4), (3, 5), (4, 3), (4, 4), (4, 5) ]
    cells = [ (2, 4), (2, 5), (1,5 ), (1, 6), (3, 5)]
    game.set_cells(cells)

    while True:
        
        try:
            
            game.print_world() 
            game.run()
            if not game.everyone_alive():
                print("everyone died")
                break
            time.sleep(0.1)
        except:
            break

if __name__ == "__main__":
    main()
    
