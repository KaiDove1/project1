# Kai Dove : ybr8ff 
# James Xu : ??????

#1a.
#Astronomy, Calculus, French, History
# Astronomy, Calculus, French, Literature
# Astronomy, Calculus, French, Organic Chemistry
# Astronomy, Calculus, French, Physics
# Astronomy, Calculus, History, Literature
# Astronomy, Calculus, History, Organic Chemistry
# Astronomy, Calculus, History, Physics
# Astronomy, Calculus, Literature, Organic Chemistry
# Astronomy, Calculus, Literature, Physics
# Astronomy, Calculus, Organic Chemistry, Physics
# Astronomy, French, History, Literature
# Astronomy, French, History, Organic Chemistry
# Astronomy, French, History, Physics
# Astronomy, French, Literature, Organic Chemistry
# Astronomy, French, Literature, Physics
# Astronomy, French, Organic Chemistry, Physics
# Astronomy, History, Literature, Organic Chemistry
# Astronomy, History, Literature, Physics
# Astronomy, History, Organic Chemistry, Physics
# Astronomy, Literature, Organic Chemistry, Physics

#1b.
# 9am: Calculus, 10am: Physics, 11am: Organic Chemistry, 12pm: History
# 9am: Calculus, 10am: Physics, 11am: Organic Chemistry, 12pm: Literature
# 9am: Calculus, 10am: Physics, 11am: Organic Chemistry, 12pm: French
# 9am: Calculus, 10am: Physics, 11am: Organic Chemistry, 12pm: Astronomy
# 9am: Calculus, 10am: Physics, 11am: History, 12pm: Literature
# 9am: Calculus, 10am: Physics, 11am: History, 12pm: French
# 9am: Calculus, 10am: Physics, 11am: History, 12pm: Astronomy
# 9am: Calculus, 10am: Physics, 11am: Literature, 12pm: French
# 9am: Calculus, 10am: Physics, 11am: Literature, 12pm: Astronomy
# 9am: Calculus, 10am: Physics, 11am: French, 12pm: Astronomy
# 9am: Calculus, 10am: Organic Chemistry, 11am: History, 12pm: Literature
# 9am: Calculus, 10am: Organic Chemistry, 11am: History, 12pm: French
# 9am: Calculus, 10am: Organic Chemistry, 11am: History, 12pm: Astronomy
# 9am: Calculus, 10am: Organic Chemistry, 11am: Literature, 12pm: French
# 9am: Calculus, 10am: Organic Chemistry, 11am: Literature, 12pm: Astronomy
# 9am: Calculus, 10am: Organic Chemistry, 11am: French, 12pm: Astronomy
# 9am: Calculus, 10am: History, 11am: Literature, 12pm: French
# 9am: Calculus, 10am: History, 11am: Literature, 12pm: Astronomy
# 9am: Calculus, 10am: History, 11am: French, 12pm: Astronomy
# 9am: Calculus, 10am: Literature, 11am: French, 12pm: Astronomy

#1c.
# Counts the possible book orders, due to a triple iteration of the list "books" and incrementing orders by 1 for every combination.

#1d.
courses = ["Calculus", "Physics", "Organic Chemistry", "History", "Literature", "French", "Astronomy"]
book_orders = []
count = 0

for i in courses:
    for j in courses:
        for k in courses:
            for l in courses:
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    book_orders.append([i, j, k, l])
                    count += 1

for index, order in enumerate(book_orders[:20]):
    print(f"{index+1}. {', '.join(order)}")

print(f"Total number of book orders: {count}")

# 7 P 4 = 840

#2a.
count2 = 0

for i in range(256): # 2^8 
    binary_string = format(i, '08b') #i --> 8 bit bin string
    if binary_string.count('0') == 3 and binary_string.count('1') == 5:
        print(binary_string)
        count2 += 1

print(f"Total number of binary strings/passwords: {count2}") 

# 8 C 3 

#Explanation : Goes through numbers 0 to 255, representing all possible 8-bit binary combinations/passwords. Each number is converted to an 8-bit binary string.
# The script then counts the amount of 0 and 1s to the required amount the prints the binary string and increments the count2 by 1.


#2b.

# A 30 - digit password required to have 13 "0" and 17 "1" characters would have 119759850 possible passwords, which I used using the calculator's C "combination" function with 30 C 13.
# This gets every combination of that meets the requirments of the required amount of "0s" then increases the resulting combinations count by 1 due to the fact that the order does not matter.