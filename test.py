# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#   for pixel in row:
#     if pixel == '1':
#       print("*", end ='')
#     else:
#       print(" ", end ='')
#   print('')

def highest_even(li):
  even_nums = []
  highest_even = 0
  for number in li:
    if number % 2 == 0:
      even_nums.append(number)

  for even_num in even_nums:
    if even_num > highest_even:
      highest_even = even_num

  return highest_even

   

print(highest_even([10,2,3,4,8,11]))