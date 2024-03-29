def roman_to_int(roman):
   romans_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
   conversion = 0
   for index, letter in enumerate(roman):
      if index + 1 < len(roman):
         if romans_values[str.upper(roman[index + 1])] > romans_values[str.upper(letter)]:
            conversion -= romans_values[f"{str.upper(letter)}"]
         else:
            conversion += romans_values[f"{str.upper(letter)}"]
      else:
         conversion += romans_values[f"{str.upper(letter)}"]
   return conversion


conversion = roman_to_int(list(roman := str(input("[+] ENTER THE DESIRED ROMAN NUMBER: "))))
print(f"{str.upper(roman)} = {conversion}")

# print(f"{roman_to_int(list(roman := str(input('[+] ENTER THE DESIRED ROMAN NUMBER: '))))} = {str.upper(roman)}")