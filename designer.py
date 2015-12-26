import random


class CellDesigner(object):
    def __init__(self, max_point=7, max_gene_length=10, genome=[]):
        self.genome = genome
        self.max_point = max_point
        self.max_gene_length = max_gene_length
        
    def generate_genome(self):
        length = random.randint(1, self.max_gene_length)
        print(length)
        for l in range(length):
            gene = self.generate_gene() 
            self.genome.append(gene)

    def generate_gene(self):
        x = random.randint(0, self.max_point)
        y = random.randint(0, self.max_point)
        x_dir = random.choice([1, -1])
        y_dir = random.choice([1, -1])
        return ((x * x_dir), (y * y_dir))

    def generate_cells(self, x, y):
        cells = []
        for item in self.genome:
            x_move, y_move = item

            new_x = x + x_move
            if new_x > self.max_point:
                new_x = new_x - self.max_point
            if new_x < 0:
                nex_x = self.max_point + new_x

            new_y = y + x_move
            if new_y > self.max_point:
                new_y = new_y - self.max_point
            if new_y < 0:
                new_y = self.max_point + new_y
            cells.append((new_x, new_y))
        return cells

    def cross_breed(self, seq_x, seq_y):
        if len(seq_x) > len(seq_y):
            main_seq = seq_x
            secondary_seq = seq_y
        else:
            main_seq = seq_y
            secondary_seq = seq_x

        for i in range(len(main_seq)):
            gene = random.choice([ main_seq, secondary_seq ])
            if i > len(gene):
                continue
            self.genome.append(gene[i])
    
    def mutate(self, sequence):
        # Just mutate one gene
        for i in sequence:
            mutate = random.choice([ True, False ])
            if mutate:
                gene = self.generate_gene()
                self.genome.append(gene)
            else:
                self.genome.append(i)

    def destroy(self):
        self.genome = []


class GeneBank(object):
    def __init__(self):
        self.bank = []

    def add_gene(self, sequence):
        self.bank.append(sequence)

    def random_choice(self):
        if not self.bank:
            return None
        return random.choice(self.bank)
