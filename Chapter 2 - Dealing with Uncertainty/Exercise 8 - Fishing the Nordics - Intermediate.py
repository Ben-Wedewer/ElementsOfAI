def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here
    i = 0
    while i < len(countries):
        prob = fishers[i]/total_fishers
        populations[i] = prob
        i += 1
    #return prob

    for country, population in zip(countries, populations):
        print("%s %.2f%%" % (country, population *100)) # modify this to print correct results

main()
