record= input("Enter a text here: ")

slowed_text = ""
for char in record:
    if char == " ":
        slowed_text += "..."
    else:
        slowed_text+= char

print(slowed_text)
