def get_user_data():
 user_data = {}

      
 name1 = input("Enter your name: ")
 user_data.update({"name" : name1})
 height1 = int(input("Enter your height: "))
 user_data.update({"height" : height1})
 weight1 = int (input("Enter your weight: "))
 user_data.update({"weight" : weight1})
 return user_data