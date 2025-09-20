input_str = "teeterababc"

for char in input_str:
   if input_str.count(char) == 1:
      print("First character which is not repeated is: ", char)
      break


