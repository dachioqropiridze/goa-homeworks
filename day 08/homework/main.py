# დავალება 2


print(True and False or False or True and False)    # False


# დავალება 3


number = int(input("enter number: "))

if number %2 == 0 and number > 10:
    print(True)
else: print(False)


# დავალება 4



# დავალება 5


# for loops ფუნქცია გამოიყენება როდესაც თქვენ გაქვთ
# კოდის ბლოკი, რომლის გამეორებაც გსურთ განსაზღვრული
# რაოდენობის განმავლობაში.
# for loops ყოველთვის გამოიყენება ინტერამენტულ ობიექტთან
# ერთად, როგორიცაა სია ან დიაპაზონი.
# პითონი განცხადებებისთვის იზეირებს თანმიმდევრობის წევრებს,
# ყოველ ჯერზე ასრულებს ბლოკს.


# დავალება 6


for i in range(1 , 16):
    print(i)


# დავალება 7


result = 0
for i in range(1 , 10):
    result += i

print(result)