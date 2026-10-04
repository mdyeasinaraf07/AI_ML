n = int(input())
num = input()
num_split = num.split()

even = 0
odd = 0
positive = 0
negative = 0

for i in range (n):
    if int(num_split[i]) > 0:
        positive += 1
    elif int(num_split[i])  < 0:
        negative += 1

    if int(num_split[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)