#!/usr/bin/env python

import room_home
import room_puzzle
import global_vars
import sys
import random

welcome='''
welcome to demo 1.0
syntax is simple and short'''

'''
puzzle is south of start
viable actions are as follows
  s
  n
  import flashlight
  read page
  solve puzzle
'''

def error(input):
    print("You typed: {0}").format(input)
    action=str(raw_input("Try again:\n"))
    return action


action="start"
lit=False
global_vars.key=random.randint(1,65536)

print welcome
while 1:
  print("--------------------")
  if action=="start": action=room_home.start_default(None)
  elif action=="south": action=room_puzzle.puzzle_default(None)
  elif action=="read page": action=room_home.read_page("start")
  elif action=="s": action=room_puzzle.puzzle_default(None)
  elif action=="n": action=room_home.start_default(None)
  elif action=="solve puzzle": action=room_puzzle.solve_puzzle(None)
  elif action==global_vars.key: break
  else: action=error(action)
print("you won or you cheated, either way, you're out of code")
sys.exit(0)
