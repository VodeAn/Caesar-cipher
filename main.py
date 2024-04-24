while True:
  print("""
                                                   .__       .__                  
  ____  ____ _____    ______ ___________    ____ |__|_____ |  |__   ___________ 
_/ ___\/ __ \\__  \  /  ___// __ \_  __ \ _/ ___\|  \____ \|  |  \_/ __ \_  __ \
\  \__\  ___/ / __ \_\___ \\  ___/|  | \/ \  \___|  |  |_> >   Y  \  ___/|  | \/
 \___  >___  >____  /____  >\___  >__|     \___  >__|   __/|___|  /\___  >__|   
     \/    \/     \/     \/     \/             \/   |__|        \/     \/     
  
        """)
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      if char in alphabet:

        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char


    print(f"Here's the {cipher_direction}d result: {end_text}")

  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    break
  else:
    continue

