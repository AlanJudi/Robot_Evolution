import population
import simulation
import numpy as np
import genome
import creature

pop = population.Population(pop_size=20, gene_count=3)
sim = simulation.ThreadedSim(pool_size=8)

for generation in range(10):
    #Evaluate first population
    sim.eval_population(pop,2400)

    #Get fitness and fitness map
    fits = [cr.get_distance_travelled() for cr in pop.creatures]
    fitmap = population.Population.get_fitness_map(fits)
  
    new_gen = []
    elite = None
    print(generation, np.max(fits), np.mean(fits))
    
    fmax = np.max(fits)
    
    for cr in pop.creatures:
        if cr.get_distance_travelled() == fmax:
            elite = cr
            break
            

    for cid in range(len(pop.creatures)):
        
        #Parent Selection
        p1_ind = population.Population.select_parent(fitmap)
        p2_ind = population.Population.select_parent(fitmap)
        
        #Cross over step
        dna = genome.Genome.crossover(pop.creatures[p1_ind].dna, pop.creatures[p2_ind].dna)
        print(dna)
        #Mutation
        dna = genome.Genome.point_mutate(genes=dna,rate=0.3, amount=0.25)
        dna = genome.Genome.grow_mutate(genes=dna, rate=0.25)
        dna = genome.Genome.shrink_mutate(genes=dna, rate=0.25)
        
        cr = creature.Creature(1)
        cr.set_dna(dna=dna)
        new_gen.append(cr)
        
    new_gen[0] = elite
    pop.creatures = new_gen



