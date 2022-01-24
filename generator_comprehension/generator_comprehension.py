# Generator 1
gen_1 = (i/100 for i in [-1000, -900, -800, 200, 300, 400, 500, 600, 7000])

# Generator 2 combined with Generator 1
gen_2 = (n for n in gen_1 if n >= 0)

# Print sum of gen_2
print(sum(gen_2))
