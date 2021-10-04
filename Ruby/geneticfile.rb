require_relative('item.rb')
require_relative('knapsack.rb')

if ARGV.length > 0
  num_items = ARGV[0].chomp.to_i
  num_knapsacks = ARGV[1].chomp.to_i
  num_generations = ARGV[2].chomp.to_i
  verbose = ARGV[3]
  if verbose == "true"
    verbose = true
  else
    verbose = false
  end
end

items = []
knapsacks = []
generation = 1

# Generate random items
num_items.times do
  ran_weight = (rand * 10).round(2)
  ran_value = (rand * 100).round(2)
  items << Item.new(ran_weight, ran_value)
end

# Generate initial knapsacks
num_knapsacks.times do 
  ran_items = []
  num_items.times do
    if rand < 0.1
      ran_items << 1
    else
      ran_items << 0
    end
  end
  knapsacks << Knapsack.new(ran_items)
end

# Main loop
until generation > num_generations
  
  puts "==================================" if verbose
  puts "Begin generation: " + generation.to_s if verbose
  puts "==================================" if verbose

  sum_value = 0.0
  best_value = 0.0
  best_knapsack = 0
  max_weight = 50.0

  # Calculate value and weight
  knapsacks.each_with_index do |knapsack, index|
    total_weight = 0.0
    total_value = 0.0
    knapsack.chromosome.each_with_index do |gene, gene_index|
      if gene === 1
        total_weight += items[gene_index].weight
        total_value += items[gene_index].value
      end
    end
    if total_weight <= max_weight
      if total_value > best_value
        best_value = total_value
        best_knapsack = index
      end
    else 
      total_value = 0.0
    end
    knapsack.total_weight = total_weight
    knapsack.total_value = total_value
    sum_value += total_value
  end

  # Use Roulette wheel algorithm to proportionately create next generation
  new_generation = []
  elitist = Knapsack.new(knapsacks[best_knapsack].chromosome.clone)
  puts 'Elitist: ' + best_knapsack.to_s if verbose
  p elitist if verbose
  (num_knapsacks-1).times do
    rnd = rand();
    rnd_sum = 0.0
    rnd_selected = 0;

    knapsacks.each do |knapsack|
      rel_value = knapsack.total_value / sum_value
      rnd_sum += rel_value
      if rnd_sum > rnd
        break
      else
        rnd_selected += 1
      end
    end
    new_generation << Knapsack.new(knapsacks[rnd_selected].chromosome.clone)
  end

  # Replace old generation with new
  knapsacks = []
  knapsacks = new_generation
  generation += 1

  # Randomly select two knapsacks
  rnd_knap_1 = (0...num_knapsacks-1).to_a.sample
  rnd_knap_2 = rnd_knap_1
  until (rnd_knap_2 != rnd_knap_1)
    rnd_knap_2 = (0...num_knapsacks-1).to_a.sample
  end

  # Perform crossover
  split_point = (0...num_items-1).to_a.sample
  front_1 = knapsacks[rnd_knap_1].chromosome[0, split_point];
  front_2 = knapsacks[rnd_knap_2].chromosome[0, split_point];
  back_1 = knapsacks[rnd_knap_1].chromosome[split_point, num_items-1];
  back_2 = knapsacks[rnd_knap_2].chromosome[split_point, num_items-1];
  new_chr_1 = front_1 + back_2
  new_chr_2 = front_2 + back_1
  new_1 = Knapsack.new(new_chr_1)
  new_2 = Knapsack.new(new_chr_2)

  knapsacks[rnd_knap_1] = new_1
  knapsacks[rnd_knap_2] = new_2

  # Perform mutation
  knapsacks.each do |knapsack|
    knapsack.chromosome.each_with_index do |gene, index|
      if rand < 0.01
        puts 'Successful mutation at gene: ' + index.to_s if verbose
        gene == 0 ? gene = 1 : gene = 0
        knapsack.chromosome[index] = gene
      end
    end
  end

  knapsacks << elitist

  puts 'Last knapsack:' if verbose
  p knapsacks[num_knapsacks-1] if verbose
  puts 'Best value:'
  p best_value

end
