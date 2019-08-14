import re
import sys

def main():
   if(len(sys.argv)==1):
      interactiveMode()
   else:                                 # File input mode
      try:
         with open(sys.argv[1], "r") as f:
            newEvent = False             # check for syntax
            people_list = list()
            for line in f:
               list_line = line.split()
               if(len(list_line)==0):   # ignore empty lines
                  continue
               if(re.search("Event", list_line[0]) or re.search("event", list_line[0])):
                  event_name = list_line[1:]
                  newEvent = True
               elif(re.search("People", list_line[0]) or re.search("people", list_line[0])):
                  if(newEvent!=True):
                     print("Syntax Error: People names are declared before creating a new event.")
                     break

                  people_list = list_line[1:]
                  new_guy(people_list)      # add new guys to people_total
               elif(re.search("result", list_line[0]) or re.search("Result", list_line[0])):
                  final_calculation()
               else:
                  if(len(people_list)<1):
                     print("Syntax error: People's names undeclared.")
                     break

                  trans_flag = False
                  trans_flag = detailed_transaction_file(trans_flag, people_list, line.strip())
                  if(trans_flag==True):
                     print("At line: " + line)
                     break
                  newEvent = False

            f.close()
      except:
         print("Please run the program with correct form of arguments.")

def interactiveMode():
   global people_total                # global variable
   while(True):
      # get user input
      command = raw_input("Please enter command: ")

      # analyse user's input
      if(command=='Q' or command=='q' or command=='exit'):                # quit the program
         break
      elif(command=="new event" or command=="NE" or command=="ne"):       # start a new event
         # get people's names
         print("Please enter all the guys' names in English, splited them with spaces or colons or whatever shit other than English letters you wanna use:")
         people_string = raw_input()
         people_string = re.sub("[^A-Za-z]", " ", people_string)
         people_list = people_string.split()
         new_guy(people_list)

         # this is irrelevant to the program, but just for human readibility
         event = raw_input("Please enter event name:")
         print("\n current event: " + event + "     number of people: " + str(len(people_list)))

         # detailed transactions
         trans_flag = False
         while(not trans_flag):
            user_trans = raw_input(">>> ")
            trans_flag = detailed_transaction(trans_flag, people_list, user_trans)

      # show result
      elif(command=="result" or command=="Result" or command=="r" or command=="R"):
         final_calculation()
      else:
         print("Please enter either \"new event\" or \"q\" or \"result\"")

# if somebody transfer some money to another guy... (among those guys in the list)
def transfer(sender, receiver, amount):
   global people_total
   people_total[receiver][sender] += int(amount)

# if somebody pays...
def pay(person, amount, people_list):
   global people_total
   owe_list = people_list[:]
   owe_list.remove(person)             # this guy doesn't own himself/herself
   share_amount = float(amount) / len(people_list)
   for guy in owe_list:
      people_total[guy][person] += share_amount

# False: continue the program
# True: throw out an error
def detailed_transaction_file(trans_flag, people_list, user_trans):
   ut_list = user_trans.split()

   if(user_trans=="q" or user_trans=="Q"):
      return False

   try:
      flag_transfer = (ut_list[1]=="T" or ut_list[1]=='t' or re.search("Trans", ut_list[1]) or re.search("trans", ut_list[1]) or ut_list[1]=="->")
      flag_pay = (ut_list[1]=="P" or ut_list[1]=="p" or re.search("Pay", ut_list[1]) or re.search("pay", ut_list[1]) or ut_list[1]=="paid")
   except:
      print("Syntax error: \"pay\" or \"trans\" unstated.")
      return True

   try:
      if(flag_transfer):
         transfer(ut_list[0], ut_list[2], ut_list[3])
      elif(flag_pay):
         pay(ut_list[0], ut_list[2], people_list)
   except:
      print("Syntax error: line argument error")
      return True

   return False

# detailed_transaction :: Bool -> List -> Bool
def detailed_transaction(trans_flag, people_list, user_trans):
   ut_list = user_trans.split()

   if(user_trans=="q" or user_trans=="Q"):
      return True

   try:
      flag_transfer = (ut_list[1]=="T" or ut_list[1]=='t' or re.search("Trans", ut_list[1]) or re.search("trans", ut_list[1]) or ut_list[1]=="->")
      flag_pay = (ut_list[1]=="P" or ut_list[1]=="p" or re.search("Pay", ut_list[1]) or re.search("pay", ut_list[1]) or ut_list[1]=="paid")
   except:
      print("Please enter valid operations. (See README.md)")
      return False

   try:
      if(flag_transfer):
         transfer(ut_list[0], ut_list[2], ut_list[3])
      elif(flag_pay):
         pay(ut_list[0], ut_list[2], people_list)
   except:
      print("Syntax error: please refer to README.md for detailed instructions.")

   return False

# create new guys in people_total
def new_guy(people_list):
   global people_total
   for guy in people_list:
      if guy not in people_total:      # new guy
         people_total[guy] = dict()    # build a new pair
         other_mfs = people_list[:]
         other_mfs.remove(guy)         # a list of people except this guy
         for other_motherfuckers in other_mfs:
            people_total[guy][other_motherfuckers] = 0
            if(other_motherfuckers in people_total):
               people_total[other_motherfuckers][guy] = 0

def final_calculation():
   global people_total
   for sender in people_total:
      for receiver in people_total[sender]:
         if(people_total[sender][receiver] >= people_total[receiver][sender]):    # counteract
            people_total[sender][receiver] -= people_total[receiver][sender]
            people_total[receiver][sender] = 0

   # finally we got there
   for folks in people_total:
      print(folks + " " + str(people_total[folks]))

# global variables
people_total = dict(dict())                # people : money

if __name__ == '__main__':
   main()


