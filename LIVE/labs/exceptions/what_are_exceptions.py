Function signature and docstring:
def get_string_from_user(msg):
  """
    Summary:
      Asks the user to enter a string and
      - if any error occurs => print:
        "***Oops, something went wrong! Try again!" and ask again

      Returns the user input, as string, when no errors occurred.

    Usage:
      user_input = get_string_from_user("enter a user name: ")

    Arguments:
      msg {[string]} -- [the string to be displayed to the user,]

    Returns:
      [string] -- [the string entered from user]
  """

user_name = get_string_from_user("enter a user name: ")
user_town = get_string_from_user("enter a user town: ")