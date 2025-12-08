import mysql.connector as connector 

mydb = connector.connect(host="localhost",user="root",password="1234",database="personal_pc")
db_cursor = mydb.cursor()

def create_table():
    try:
        db_cursor.execute("CREATE TABLE games(name VARCHAR(100) UNIQUE NOT NULL,size VARCHAR(10) NOT NULL)")
        mydb.commit();
    except :
        print("Table already exists")

def addGame(game_name,game_size):
    db_insert = "INSERT INTO games(name,size) values(%s,%s)"
    insert_value = (game_name,game_size);
    db_cursor.execute(db_insert,insert_value);
    print("Game added succesfully");
    mydb.commit();

def showgame():
    print("------------------- AVAILABLE GAMES--------------")
    db_cursor.execute("SELECT * FROM games");
    for game in db_cursor:
        print(f"Game Name : {game[0]} Size: {game[1]}GB");

def deletegame(game_name):
    db_cursor.execute("DELETE FROM games WHERE name=%s",(game_name,));
    mydb.commit();
    print("game deleted succesfully")

def updategamesize(game_name,game_size):
    db_cursor.execute("UPDATE games SET size=%s WHERE name=%s",(game_size,game_name))
    mydb.commit();
    print("game Updated")

c=1
print("1. Create Game section.")
print("2. To add Game.")
print("3. To view Games.")
print("4. To Delete game.")
print("5. To Update Game.")
print("5. Exit.")
while(c!=6):
    c = int(input("enter choice: "))
    if(c==1):
        create_table();
    elif(c==2):
        game_name = input("Game Name: ")
        game_size = input("Game Size: ")
        addGame(game_name,game_size);
    elif(c==3):
        showgame();
    elif(c==4):
        game_name = input("Enter game you want to delete: ");
        deletegame(game_name);
    elif(c==5):
        game_name = input("Enter game you want to update: ")
        game_size = input("Enter New Size of game : ");
        updategamesize(game_name,game_size);
    elif(c==6):
        print("Thank You for using")
        break
    else:
        print("wrong input!");





