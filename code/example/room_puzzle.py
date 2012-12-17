import global_vars

room_description='''
this room contains a puzzle
exits are north'''

def puzzle_default(call):
  print room_description
  if call is not None:
    action=call
  else:
    action=str(raw_input("What do you want to do?\n"))
  return action

def solve_puzzle(call):
  print room_description
  if call is not None:
    action=call
  else:
    action=int(raw_input("What is the key to solve the puzzle\n"))
  if action==global_vars.key:
    print("hooray, you have solved the puzzle")
    return action
  else:
    print("wrong key, you will need to get the key first!")
    action="s"
    return action