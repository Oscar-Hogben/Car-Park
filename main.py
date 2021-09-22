from datetime import datetime
import time
import os


spaces = 100
now = datetime.now()
parkingCode = 100000
code = 100000
overstayed = 0
moneyMade = 0
totalCars = 0
averagePaid = 0
avergeStayed = 0
totalStayed = 0

loop = True
while loop == True:

  file = open("Stats/Spaces", "w")
  file.write(str(spaces))
  file.close()

  file = open("Stats/Overstayed", "w")
  file.write(str(overstayed))
  file.close()

  file = open("Stats/Money Made", "w")
  file.write(str(moneyMade))
  file.close()

  file = open("Stats/Total Cars", "w")
  file.write(str(totalCars))
  file.close()

  timestamp = time.strftime('%H')
  unixTime = round(time.time())
  print("Press enter to continue.")
  if input() == "time change":
    timestamp = input("Enter the time: ")
    unixTime = input("Enter the specific time: ")
  #timestamp = 0                   # Quick time changer
  #spaces = 0                      # Quick space changer
  if int(timestamp) < 21 and int(timestamp) >= 5:
    print("Are you leaving or entering?")
    direction = input().lower()

    if direction == "entering":
      if spaces > 0:
        code = code +1
        print("Welcome to the carpark!")
        print()
        print("There are", spaces, "spaces left")
        print()
        print("Press enter to get a ticket number!")
        input()
        print(f'''
{code}, is your parking code! REMEMBER IT!!!
Please leave before 9 pm, do not stay longer
than 8 hours!
        ''')
        file = open(f"Tickets/{str(code)}", "w")
        time.sleep(5)
        file.write(str(unixTime))
        time.sleep(5)
        file.close()
        spaces = spaces - 1
        file = open("Stats/Spaces", "w")
        file.write(str(spaces))
        file.close()

        totalCars = totalCars + 1
        os.system('clear')
      else:
        os.system('clear')
        print('''
Sorry there are no available spaces right now.
Please come back later!
        ''')
        time.sleep(10)
        os.system('clear')
    
    elif direction == "leaving":
      print("Please enter your parking number: ")
      number = input()
      file = open(f"Tickets/{str(number)}", "r")
      timeArrived = file.read()

      file.close()

      hours = ((int(unixTime) - int(timeArrived))/3600)

      hoursPos = str(hours).find(".")

      if hoursPos == 1:
        hours = int(str(hours)[0:1])
      elif hoursPos == 2:
        hours = int(str(hours)[0:2])
      else:
        exit("An unexpected error occured!")
      

      if hours <= 1:
        print("Please pay £1.50")
        time.sleep(5)
        print("Thank you!")
        time.sleep(10)
        os.system('clear')
        moneyMade = moneyMade + 1.50
        spaces = spaces +1
        totalStayed = totalStayed + 1

      elif hours <= 8:
        print("Please pay £", 1.50 * (hours+1))
        time.sleep(5)
        print("Thank you!")
        time.sleep(10)
        os.system('clear')
        spaces = spaces +1
        moneyMade = moneyMade + (hours+1)*1.50
        totalStayed = totalStayed + (hours + 1)
      else:
        print("You have stayed over the maxemum amount of time. There will be an extra £100 charge.")
        print()
        print("Please pay £", ((hours+1)*1.50)+100)
        time.sleep(5)
        moneyMade = moneyMade + ((hours+1)*1.50)+100
        print("Thank you!")
        time.sleep(10)
        os.system('clear')
        spaces = spaces +1
        overstayed = overstayed +1
        totalStayed = totalStayed + (hours + 1)


  else:
    print("The carpark is curently closed!")
    time.sleep(10)
    os.system('clear')
    
    if int(timestamp) == 0:
      loop2 = 9999
      spaces = 100
      codeRemove = 100000
      print(overstayed, "cars have overstayed today.")
      time.sleep(5)
      os.system('clear')
      print("£", moneyMade, "made today")
      time.sleep(5)
      os.system('clear')
      print("The total cars that used the carpark today:", totalCars)
      time.sleep(5)
      os.system('clear')
      if moneyMade != 0 and totalCars != 0:
        print("There was an average of", moneyMade/totalCars, "spent today!")
        time.sleep(5)
        os.system('clear')
      
      if totalStayed != 0 and totalCars != 0:
        print("There was an average of", totalStayed / totalCars,"hours cars were using the carpark")
        time.sleep(5)
        os.system('clear')
      parkingCode = 100000
      code = 100000
      overstayed = 0
      moneyMade = 0
      totalCars = 0
      averagePaid = 0
      avergeStayed = 0
      totalStayed = 0
      while loop != 0:
        os.system('clear')
        print("Resetting (the carpark is currently closed!)")
        codeRemove = codeRemove + 1
        file = open(f"{codeRemove}", "w")
        os.remove(f"{codeRemove}")
        file.close()


      

