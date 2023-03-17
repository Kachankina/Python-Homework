
def show_data():
    with open ('Seminar8/data.txt' , 'r' , encoding= 'utf-8') as data :
    
        return data.read().split('\n')

def new_data():
    with open ('Seminar8/data.txt' , 'a' , encoding= 'utf - 8')  as file:
        temp = input(('Insert data:')+ '\n')
        file.write(temp)
        
def find_data():
    with open ('Seminar8/data.txt' , 'r' , encoding= 'utf - 8')  as file:
      
        book = file.read().split('\n')
        temp = input()
        for i in book:
           if temp in i:
              print(i)
       
def delete_data():
    book =  open('Seminar8/data.txt' , 'r' , encoding= 'utf - 8') 
    phonebook = book.readlines()
    contact = (input())                                               
    for i  in range (len(phonebook)):
        if contact in phonebook[i]:
            phonebook[i] = ''
    with open('Seminar8/data.txt' , 'w' , encoding= 'utf - 8') as file:
         file.writelines(phonebook)
    
       
def change_data():
    with open ('Seminar8/data.txt' , 'r' , encoding= 'utf - 8')  as file:
        lines = file.readlines()
        exist_contact = (input())
        new_contact = (input())
    with open ('Seminar8/data.txt' , 'w' , encoding= 'utf - 8')  as file:
         for line in lines:
            line = line.strip()
            if line == exist_contact:
                file.writelines(new_contact)
            else:
                file.writelines(line)
        
   
   
   
            
while True:
    mode = input('Choose book mode:')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        delete_data()
    elif mode == '5':
        change_data()
    elif  mode == '0':
        break
    else:
        print('No mode')
    
        