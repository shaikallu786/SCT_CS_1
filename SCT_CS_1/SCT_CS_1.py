def caesar_cipher(text, shift, mode='encrypt'):
  """Encrypt or decrypt text using the Caesar cipher algorithm.

  Args:
      text (str): The text to be encrypted or decrypted.
      shift (int): The number of positions to shift the alphabet.
      mode (str): 'encrypt' to encrypt, 'decrypt' to decrypt. Default is 'encrypt'.

  Returns:
      str: The encrypted or decrypted text.
  """
  if mode not in ['encrypt', 'decrypt']:
      raise ValueError("Mode must be 'encrypt' or 'decrypt'.")

  if mode == 'decrypt':
      shift = -shift

  encrypted_text = ''
  for char in text:
      if char.isalpha():
          shift_base = ord('A') if char.isupper() else ord('a')
          new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
          encrypted_text += new_char
      else:
          encrypted_text += char

  return encrypted_text

def main():
  print("Caesar Cipher Program")
  while True:
      choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().lower()
      if choice == 'q':
          print("Exiting the program.")
          break
      elif choice in ['e', 'd']:
          text = input("Enter your message: ").strip()
          try:
              shift = int(input("Enter the shift value (integer): ").strip())
          except ValueError:
              print("Invalid shift value. Please enter an integer.")
              continue

          mode = 'encrypt' if choice == 'e' else 'decrypt'
          result = caesar_cipher(text, shift, mode)
          print(f"Result: {result}")
      else:
          print("Invalid choice. Please select (E)ncrypt, (D)ecrypt, or (Q)uit.")

if __name__ == "__main__":
  main()
