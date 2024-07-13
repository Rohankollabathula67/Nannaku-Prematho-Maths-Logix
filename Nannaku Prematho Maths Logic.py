def nth_person_alive(n):
    powers_of_2 = [ 2 ** i for i in range(1,51)]
    if n == 1 :
        return 1
    for j in range(n):
        if  powers_of_2[j] > n :
            toNegative = powers_of_2[j-1]
            break
    return (n - toNegative)*2 + 1
        
n = 100
result = nth_person_alive(n)

print(f"{result} Person will alive")
