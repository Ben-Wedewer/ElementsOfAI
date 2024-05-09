def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    def check_if_all_numbers_exist(array):
                            return all(number in array for number in range(1, 5))
                    result = check_if_all_numbers_exist(route)
                    #print(result)
                    # Modify this if statement to check if the route is valid
                    if(result):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()