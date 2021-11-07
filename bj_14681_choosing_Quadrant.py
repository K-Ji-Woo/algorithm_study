# x
# y

# if x 양수
#     if y 양수 -> 1
#     elif y 음수 -> 4
# elif x 음수 
#     if y 양수 -> 2
#     elif y 음수 -> 3

    

x = int(input())
y = int(input())

if x > 0 :
    if y > 0 :
        print("1")
    elif y < 0 :
        print("4")
elif x < 0 :
    if y > 0 :
        print("2")
    elif y < 0 :
        print("3")