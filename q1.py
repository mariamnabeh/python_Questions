"""
1. Use a loop to display elements from a given list present at odd index positions
Input:
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output:
20 40 60 80 100
"""
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in list[1:11:2]:
  print(i,end=" ")
