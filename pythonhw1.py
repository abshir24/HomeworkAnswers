# Print the sum of all numbers from 1-15

sum = 0
for i in range(1,15):
    sum+=i

print("SUM",sum)

# FIZZ BUZZ

for i in range(1,100):
    if i%2 == 0:
        print("FIZZ")
    else:
        print("BUZZ")

# MAX MIN AND AVERAGE

numbers = [1,2,3,4,5]

print(f'Max {max(numbers)}, Min {min(numbers)}, Average {sum(numbers)/len(numbers)}')