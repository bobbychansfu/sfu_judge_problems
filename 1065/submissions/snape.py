ingredients = {
  "before 9am": ["Boomslang skin", "Hair of the person you want to turn into", "Horn of bicorn", "Leeches"],
  "9am": ["Occamy eggshell", "Ashwinder egg", "Dash of tincture of thyme", "Goldfish"] 
}

inp = input("Enter class time (i.e. 8:30, 9:00, 13:30, etc.): ").split(":")
input_time = int(inp[0])
input_mins = int(inp[1])
if input_time == 9 and input_mins == 0:
  print("Boomslang skin, Hair of the person you want to turn into, Horn of bicorn, Leeches")
elif input_time < 9:
  print("Occamy eggshell, Ashwinder egg, Dash of tincture of thyme, Goldfish")  
else:
  print("No potion ingredients needed but go smack Mr. Potter!")