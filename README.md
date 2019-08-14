# Divide_the_shit_equally

## This light-weight command line applet allows you to calculate money stuffs easily.

Have you ever encountered such a situation:

You, Allen, Alex, and Lily had a fantastic day. However, you paid for the lunch, Allen paid for the Uber ride, Alex booked four movie tickets online for Avengers 5, and Lily transfered Allen 40 bucks mistakenly. <br>

You folks want to divide the money equally but it seems so freakingly involved to get a correct amount of money to whom each one should transfer. Probably even James, the guy who is super frigging good at maths, will also be stuck by this problem… for 30 seconds. <br>



### Don't worry

**Divide_the_shit_equally** comes to help.





# How do I install it?

## For programmers

open terminal (or your favorite command line tool)

run  $ git clone git@github.com:JamesSMF/divide_the_shit_equally.git

run money.py inside the git directory diectly.



## For non-programmers

Prepare a mac

click the green button "clone or download"

![Screen Shot 2019-08-14 at 6.55.48 PM](/Users/liguangyao/Desktop/Screen Shot 2019-08-14 at 6.55.48 PM.png)



Click **Download ZIP**

Open System Preference -> Security & Privacy

Click the small lock and enter your password (Do I seem like a fraud…? Trust me tho lol.)

![Screen Shot 2019-08-14 at 6.57.33 PM](/Users/liguangyao/Desktop/Screen Shot 2019-08-14 at 6.57.33 PM.png)

Click the small plus sign and select Downloads -> Divide_the_shit_equally-master -> Divide_the_shit_equally



(There are 2 options for the next step)

**If you know how to use spotlight search:**

   Press command + <space> and type "Divide_the_shit_equally" (without quotation marks) and press enter.

**else:**

   Open the Finder, and go to Downloads -> Divide_the_shit_equally-master. Click the Divide_the_shit_equally app to run it.





# Basic Usage

run

```bash
python money.py
```

to start the program.



*Note: there is no database for the program. So each time you run the program, all the previous datas are cleared.*



## New Event

Type "New event" or "new event" or simply "ne" to create a new event. <br>

Then, the program will prompt the user to enter people's names. You can split names by any character you like, but **not English letters**. <br>

After that, enter the event name. For example, "A Fabulous day". <br>

When you see

```bash
>>>
```

at the beginning of the line, you have successfully entered "event mode"



### Event Mode

#### Basic syntax

* \<person> trans \<person> \<amount of money> 
* \<person> pay \<amount of money>

Feel free to make those verbs gramatically correct, but please try not to change the basic structure of the syntax.<br>

Enter "q" or "Q" to quit event mode and go back to normal mode.



## Result

When you type "result" or "Result", the program will enter its calculation process and soon return the final result.<br>

The result is normally in this form:

\<name> {\<person>: \<amount of money>, \<person>: \<amount of money>, ... }

...



\<name> is the person who should transfer \<amount of money> to  \<person>.



## Q

Enter "Q" or "q" to exit the program cleanly.
