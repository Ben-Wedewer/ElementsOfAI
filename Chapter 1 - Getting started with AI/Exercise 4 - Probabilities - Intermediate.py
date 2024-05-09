import random

def main():
    catprob = 0.20
    dogprob = 0.80
    if random.random() < catprob:
        print('cat')
    if random.random() < dogprob:
        print('dog')
main()
