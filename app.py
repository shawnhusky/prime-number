
n = 35
def solution(n):
    prime_nums = [] #new list

    for num in range(n):
        if num > 1: #all prime numbers are greater than 1
            for i in range(2, num): #start with 2 to num-1
                if (num % i) == 0: #if modulus 0 then not prime number
                    break   
                else:
                    prime_nums.append(num)
    return prime_nums

print(solution(35))
