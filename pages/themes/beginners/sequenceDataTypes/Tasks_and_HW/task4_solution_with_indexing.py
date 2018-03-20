words = ["dog", "talent", "loop", "aria", "tent", "choice"]

print("Words which starts and end with same letter are:")
for word in words:
  # if first letter is equal to last letter:
  if word[0] == word[-1]:
    print(word)
