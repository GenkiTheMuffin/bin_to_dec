num = int(input("Zadaj cislo: "))
power = 1
sol = 0
while num > 0:
    b = num % 10
    sol = sol + b * power
    power = power * 2
    num = num // 10
print(sol)
