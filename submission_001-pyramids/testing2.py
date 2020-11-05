# #How to print square
# user_input = int(input("enter height: "))
# for i in range(user_input):
#     print("* " *user_input)

# #How to print right angled triangle
# user_input = int(input("enter height: "))
# for i in range(1, user_input+1):
#     print("* " *i)

#  #How to get pyramid shape
# user_input = int(input("enter height: "))
# for i in range(1,user_input+1):
#      print(" " *(user_input-i) + "*" *(2*i-1))


#outline_pyramid
# user_input_height = int(input("whats your row: "))
# for i in range(1, user_input_height+1):
#     for j in range(1, 2*user_input_height):
#         if i == user_input_height or i + j == user_input_height+1 or  j - i == user_input_height-1:
#             print("*", end = "")
#         else:
#             print(end=" ")
#     print()


# outline_triangle
# user_input_height = int(input("whats your row: "))
# for i in range(user_input_height):
#     for j in range(user_input_height):
#         if j == 0 or i == (user_input_height-1) or i == j:
#             print("*" ,end = "")
#         else:
#             print(end = " ")
#     print()


#outline_square
# user_input_height = int(input("enter height: "))
# for i in range(user_input_height):
#     for j in range(user_input_height):
#         if i == 0 or i == user_input_height-1 or j == 0 or j == user_input_height-1:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print("")

#print rectangle
# user_input_height = int(input("height?: "))
# for i in range(1,user_input_height):
#     for j in range(1,user_input_height+3):
#         print("*", end = " ")
#     print("")

#outline_rectange
# user_input_height = int(input("height:? "))
# for i in range(1,user_input_height):
#     for j in range(1,user_input_height*2):
#         if i == 1 or i == (user_input_height-1) or j == 1 or j == ((user_input_height*2 -1)):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# solid
#     for i in range(1,user_input_height):
#             for j in range(1,user_input_height*2):
#                 print("*", end = " ")
#             print("")

# # user_input_height = int(input("height:? "))
# for i in range(1,user_input_height+1):
#     print(" " *(user_input_height-i) + "*" *(2*i -1))
    
# user_input_height = int(input("Height: "))
# #top
# for i in range(1, user_input_height+1):
#     for j in range(1, user_input_height-i+1):
#         print(" ", end = "")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i -1:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()
# #bottom
# for i in range(user_input_height-1, 0, -1):
#     for j in range(1, user_input_height-i+1):
#         print(" ", end = "")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i -1:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print("")

# user_input_height = int(input("Height: "))
# for i in range(user_input_height):
#     print(" " *(user_input_height-i-1) + "* " *(i+1))
# for j in range(user_input_height-1, 0, -1):
#     print(" "*(user_input_height-j) + "* " *(j))


# user_input_height = int(input("height?: "))
# for i in range(user_input_height):
#     for j in range(user_input_height-i):
#         print(" ", end = " ")
#     for j in range(2*i+1):
#         print("*", end = " ")
#     print()

# for i in range(user_input_height):
#     for j in range(user_input_height-i):
#         print(" ", end = " ")
#     for j in range(2*i+1):
#         print("*", end = " ")
#     print()

# for i in range(user_input_height):
#     for j in range(user_input_height-1):
#         print(" ", end = " ")
#     print("* * *")
