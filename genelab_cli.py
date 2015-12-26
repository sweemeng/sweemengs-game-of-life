import random
import time
from designer import CellDesigner
from designer import GeneBank
from gameoflife import GameOfLife
from sense_hat import SenseHat

WHITE = [ 0, 0, 0 ]
RED = [ 120, 0, 0 ]


class Genelab(object):
    def __init__(self):
        self.survive_min = 5 # Cycle
        self.surival_record = 0
        self.designer = CellDesigner()
        self.gene_bank = GeneBank()
        self.game = GameOfLife()

    def get_start_point(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        return x, y

    def get_new_gen(self):
        if len(self.gene_bank.bank) == 0:
            print("creating new generation")
            self.designer.generate_genome()
        elif len(self.gene_bank.bank) == 1:
            print("Mutating first gen")
            self.designer.destroy()
            seq_x = self.gene_bank.bank[0]
            self.designer.mutate(seq_x)
        else:
            self.designer.destroy()
            coin_toss = random.choice([0, 1])
            if coin_toss:
                print("Breeding")
                seq_x = self.gene_bank.random_choice()
                seq_y = self.gene_bank.random_choice()
                self.designer.cross_breed(seq_x, seq_y)
            else:
                print("Mutating")
                seq_x = self.gene_bank.random_choice()
                self.designer.mutate(seq_x)
             

    def run(self):
        self.get_new_gen() 
        x, y = self.get_start_point()
        cells = self.designer.generate_cells(x, y)
        self.game.set_cells(cells)
        count = 1 
        self.game.destroy_world()
        while True:
            try:
                if not self.game.everyone_alive():
                    if count > self.survive_min:
                        # Surivival the fittest
                        self.gene_bank.add_gene(self.designer.genome)
                        self.survival_record = count

                    print("Everyone died, making new gen")
                    print("Species survived %s cycle" % count)
                    self.get_new_gen()
                    x, y = self.get_start_point()
                    cells = self.designer.generate_cells(x, y)
                    self.game.set_cells(cells)
                    count = 1

                if count % random.randint(10, 100) == 0:
                    print("let's spice thing up a little")
                    print("destroying world")
                    print("Species survived %s cycle" % count)
                    self.game.destroy_world()
                    self.gene_bank.add_gene(self.designer.genome)
                    self.get_new_gen()
                    x, y = self.get_start_point()
                    cells = self.designer.generate_cells(x, y)
                    self.game.set_cells(cells)
                    count = 1
 
                self.game.print_world() 
                self.game.run()
                count = count + 1
                time.sleep(0.1)
            except:
                print("Destroy world")
                print("%s generation tested" % len(self.gene_bank.bank))
                break

if __name__ == "__main__":
    lab = Genelab()
    lab.run()
        
