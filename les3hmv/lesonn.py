lst=[]
id=1
while True:
    n=int(input("""
     Choose your option -->
            
    1 --> Add person
    2 --> List of all people
    3 --> Update persons info
    4 --> Delete persons info
    5 --> Exit
"""))
    if n==1:
        dict1={}
        name=input("Enter your name -->")
        task=input("Enter your task-->")
        time=int(input("Enter time for task -->"))
        during=int(input("Enter during time for task -->"))
        dict1={
            'id':id,
            'name':name,
            'task':task,
            'time':time,
            'during':during
        }
        id+=1
        lst.append(dict1)
        print('-'*30)
        print('New person info added sucsessfuly')
    if n==2:
         for i in lst:
                print(f"""
id            -->{i['id']}
name          -->{i['name']}
task          -->{i['task']}
time          -->{i['time']}
during        -->{i['during']}
""")
    if n==3:
         b=True
         id=int(input('enter id of persons for update info')) 
         for i in lst:
              if i['id']==id:
                b==False
                nwn=input("Enter students new name -->")
                nts=input("Enter your new task -->")
                nti=int(input("Enter your new  time -->"))
                ndu=int(input("Enter your new during time -->"))
                i['name']=nwn
                i['task']=nts
                i['time']=nti
                i['during']=ndu
                print()
                print(f"Person with id {id} updated sucsesfully")
         if b:
               print('id',id,'not found ')

    if n==4:
         b=True
         id=int(input('enter id of person for delete -->')) 
         for i in lst:
              if i['id']==id:
                   b==False
                   lst.remove(i)
                   print()
                   print(f"person with id {id} deleted sucsesfully")
         if b:
               print('id',id,'not found ')
    if n==5:
         l=input('are you sure y/n-->')
         if l=='y' or l=='yes' or l=='YES':
              break
         else:
              continue


