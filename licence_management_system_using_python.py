# -*- coding: utf-8 -*-
"""Licence Management System Using Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LzgUwc7_01ciQdOToBVos7MlIh_p4ytg
"""

a={"ram":55,
   "hari":56,
   "krishna":44}
for name,age in a.items():
   print(name,"is",age,"years old")



from datetime import datetime , timedelta
listt={'name':[],
       'age':[],
       'category':[],
       'location':[],
       'Register_date':[],
       'Fathers_name':[],
       'Mothers_name':[],
       'blood_group':[]}
question=[{"ques": "", "ans":'',"opt":"",'a':1},{'ques': "","ans":'',"opt":"",'a':1},{ "ques": "","ans":'',"opt":"",'a':1},{"ques":"","ans":'',"opt":"",'a':1},{"ques":"","ans":"","opt":"",'a':1}]

while True:
  print()
  print()
  print("Licence Management System")
  print()
  print("Choose from the list of items: ")
  print()
  print("1. Make a new licence.")
  print("2. Check the renew of the licence.")
  print("3. Check licence printed or not.")
  print("4. Show all licence.")
  print("5. Licence according to location.")
  print("6. Licence according to age.")
  print("7. Licence according to category.")
  print("8. Exit.")
  print("9. Authority")
  print()
  choice = int(input("Enter your choice of number from above listed 1 - 7: "))

  if choice == 1:
    name=input("Enter your full name: ")
    age=int(input("Enter your age: "))
    category=input("Enter your category\nA=Bike\nB=Car\n: ").upper()
    location=input("Enter your location: ")
    register_date = input("Enter your register date (YYYY-MM-DD): ")
    datee = datetime.strptime(register_date, "%Y-%m-%d")
    Fathers_name = input("Enter your Fathers name: ")
    Mothers_name = input("Enter your mothers Name")
    blood_group = input("Enter your blood group")
    sum=0

    if age >=18:
      print("Ready for Licence Exam")
      print("Give correct Answer for passing writing exam.")
      for i in range(5):
        print(f"{question[i]['ques']}:\noptions\n{question[i]['ans']}\n{question[i]['opt']}")
        choose=int(input("enter 1 or 2 option= "))
        if question[i]['a'] == choose:
          print("correct answer")
          sum+=1
        else:
          print("Wrong answer")
        print()

      if sum < 3:
        print("You are not ready for Licence Exam.Better luck Next Time.")

      if sum >= 3:
        print("You are ready for Trail Exam")

        trail=input("enter pass or fail= ")
        if trail == "pass":
          listt['name'].append(name)
          listt['age'].append(age)
          listt['category'].append(category)
          listt['location'].append(location)
          listt['Register_date'].append(datee)
          listt['Fathers_name'].append(Fathers_name)
          listt['Mothers_name'].append(Mothers_name)
          listt['blood_group'].append(blood_group)
          print("Licence has been registered successfully.")
        else:
            print("Licence has not been registered.Better Luck Next Time.")

    elif age<1 and age > 100:
      if age<1:
        print("Age cannot be below 1.")
      else:
        print("Age cannot be above 100.")
    else:
     print("Unable to register as age is below 18.")

  elif choice == 2:
    a=input("Enter your name: ")
    b=input("Enter your Father name: ")
    c=input("Enter your Mother name: ")
    d=input("Enter your blood group: ")
    today=datetime.today()
    for i in range(len(["name"])):
      if listt["name"][i] == a and listt["Fathers_name"][i] == b and listt["Mothers_name"][i] == c and listt["blood_group"][i] == d:
        dd=listt['Register_date'][i]
        aaa=today.year-dd.year
        if (today.month,today.date) < (listt["Register_date"][i].month,listt["Register_date"][i].day):
          aaa-=1
        if aaa >=1:
          print("Licence has expired. plz renew in time.")
        else:
          print("Licence has not been expired.")

      else:
        print("Doesnt match")
  elif choice == 3:
    ab=input("Enter your name: ")
    bc=input("Enter your Father name: ")
    cd=input("Enter your Mother name: ")
    de=input("Enter your blood group: ")
    today=datetime.today()
    for i in range(len(listt["name"])):
      if listt["name"][i] == a and listt["Fathers_name"][i] == b and listt["Mothers_name"][i] == c and listt["blood_group"][i] == d:
        ddd=listt['Register_date'][i]
        printed=listt['Register_date'][i] + timedelta(days=60)
        if today >= printed:
          print("Licence has been printed.")
        else:
          days=(listt['Register_date'][i] - today).days
          print(f"Licence has not been printed and will be printed on {days} days.")
      else:
        print("Doesnt match")

  elif choice == 4:
    for i in range(len(listt["name"])):
      print(f'{listt["name"][i]}:{listt["category"][i]}')

  elif choice == 5:
    ff=False
    loc=input("enter a location= ")
    for i in range(len(listt['location'])):
      if loc == listt['location'][i]:
        print(f'{listt["name"][i]}:{listt["location"][i]}')
        ff=True
    if ff==False:
      print("No result Found.")

  elif choice == 6:
    a=int(input("Enter the age: "))
    for i in range(len(listt['age'])):
        if a >= 18 and a<=30:
          if age >= 18 and age <= 30:
            print(f'{listt["name"][i]}:{listt["age"][i]}:Young Age')
        elif a >= 31 and a<=50:
          if age >= 31 and age<=50:
            print(f'{listt["name"][i]}:{listt["age"][i]}:medium Age')
        elif a >= 51 and a<=100:
          if age >= 51 and age<=100:
            print(f'{listt["name"][i]}:{listt["age"][i]}:old Age')
        elif a <=0 and a>100:
          print("invalid age")
        else:
          print("invalid age")


  elif choice == 7:
    a=input("Enter the category: ").upper()
    for i in range(len(listt['category'])):
      if a =='A':
        if listt['category'][i] == 'A':
          print(f'{listt["name"][i]}:{listt["category"][i]}')
      elif a =='B':
        if listt['category'][i] == 'B':
          print(f'{listt["name"][i]}:{listt["category"][i]}')
      else:
        continue

  elif choice == 8:
    print("Thank you for using Licence Management System.")
    break
  elif choice == 9:
    print("Only Authority")
    password="Biratnagar"
    abc=input("Enter a password: ")
    if abc == password:
      print("Welcome Licence Management Officer.")
      print()
      print("Change Question")
      print()
      for i in range(0,len(question)):
        quest=input("Enter a question: ")
        opt1=input("Enter opt1: ")
        opt2=input("Enter opt2: ")
        ans=int(input("enter answer 1 or 2: "))
        question[i]['ques'] = quest
        question[i]['ans'] = opt1
        question[i]['opt'] = opt2
        question[i]['a'] = ans
        print("Question has been changed successfully.")
      print("All 5 Question Updated successfully.")

    else:
      print("Wrong password")
      exit()

  else:
    print(f"{choice} is invalid. Plz input the right option.")
    print()
    print()



