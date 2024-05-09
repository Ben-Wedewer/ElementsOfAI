def count11(seq):
   # define this function and return the number of occurrences as a number
   amount = 0
   i = 0   
   while i < len(seq):
       if seq[i] == 1:
           if seq[i+1] == 1:
               amount += 1
       i += 1
   return amount

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
# This code works to print out 2, but it does not pass the assert from the course. Not sure where the test is going wrong, but this code should pass.
