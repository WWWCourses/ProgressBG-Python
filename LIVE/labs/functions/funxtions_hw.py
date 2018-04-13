def get_user_data():
  """retrieves user data from the command line

  Returns:
    [dictionary] of the form:
      {
        "name" : "user_name",
        "height": "user heigth in meters",
        "weight": "user weight in kilograms"
      }
  """
  user_data = {}
  user_data["name"] = input("Enter your name:")  
  user_data["height"] = cm_to_meters( float(input("Enter your height:")) )
  user_data["weight"] = float(input("Enter your weight:"))
  
  return user_data


def calc_BMI(w,h):
  """calculates the BMI

  Arguments:
    w {[float]} -- [weight]
    h {[float]} -- [height]

  Returns:
    [float] -- [calculated BMI = w / (h*h)]
  """
  bmi  = w / (h*h)
  bmi = round(bmi, 4)
  return bmi

def calc_BMI_category(bmi):
  """Calculates the BMI category

  Arguments:
    bmi {[float]} -- [the bmi number index]

  Returns:
    [string] -- [bmi category]
  """
  if (bmi <= 18.5):
    return "Underweight"
  elif (18.5 < bmi < 24.9):
    return "Normal"
  elif (25 < bmi < 29.9): 
    return "Overweight"
  elif (bmi >= 30):
    return "Obesity"


def print_results(bmi_category):
  """[Prints the BMI category to the user ]

  Arguments:
    bmi_category {[string]} -- []
  """
  print("You are {}!".format(bmi_category))

def cm_to_meters(cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """
  return cm/100

user_data = get_user_data()
print(user_data)

bmi = calc_BMI(user_data["weight"],user_data["height"] )
print(bmi)
print(type(bmi))

bmi_category = calc_BMI_category(bmi)
print(bmi_category)

# print_results(bmi_category)