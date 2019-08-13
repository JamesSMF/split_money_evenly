import re

def main():
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
         number_people = len(people_list)

         for guy in people_list:
            if guy not in people_total:      # new guy
               people_total[guy] = dict()    # build a new pair
               other_mfs = people_list[:]
               other_mfs.remove(guy)         # a list of people except this guy
               for other_motherfuckers in other_mfs:
                  people_total[guy][other_motherfuckers] = 0
                  if(other_motherfuckers in people_total):
                     people_total[other_motherfuckers][guy] = 0

         # this is irrelevant to the program, but just for human readibility
         print("Please enter event name:")
         event = raw_input()

         print("\n current event: " + event + "     number of people: " + str(number_people))

         # detailed transactions
         trans_flag = False
         while(not trans_flag):
            trans_flag = detailed_transaction(trans_flag, people_list)

      elif(command=="result" or command=="Result" or command=="r" or command=="R"):
         final_calculation()
      else:
         print("Please enter either \"new event\" or \"q\" or \"result\"")

def transfer(sender, receiver, amount):
   global people_total
   people_total[receiver][sender] += int(amount)

def pay(person, amount, people_list):
   global people_total
   owe_list = people_list[:]
   owe_list.remove(person)
   share_amount = float(amount) / len(people_list)
   for guy in owe_list:
      people_total[guy][person] += share_amount

def detailed_transaction(trans_flag, people_list):
   user_trans = raw_input(">>> ")
   ut_list = user_trans.split()

   if(user_trans=="q" or user_trans=="Q"):
      return True

   try:
      flag_transfer = (ut_list[1]=="T" or ut_list[1]=='t' or re.search("Trans", ut_list[1]) or re.search("trans", ut_list[1]) or ut_list[1]=="->")
      flag_pay = (ut_list[1]=="P" or ut_list[1]=="p" or re.search("Pay", ut_list[1]) or re.search("pay", ut_list[1]))
   except:
      print("Please enter valid operations. (See README.md)")
      return False

   if(flag_transfer):
      transfer(ut_list[0], ut_list[2], ut_list[3])
   elif(flag_pay):
      pay(ut_list[0], ut_list[2], people_list)
   else:
      print("Syntax error: please refer to README.md for detailed instructions.")

   return False

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


