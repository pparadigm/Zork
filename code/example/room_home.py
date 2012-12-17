import global_vars
''' viable actions are:
read page'''


room_description='''
the room is well lit
there is a page on the ground
exits are south'''


def start_default(call):
    print room_description
    if call is not None:
      action=call
    else:
      action=str(raw_input("What do you want to do?\n"))
      return action
  
def read_page(call):
    if call is not None:
      action=call
    else:
      action=str(raw_input("What do you want to do?\n"))
    print("the page contains the number sequence {0}").format(global_vars.key)
    return action    