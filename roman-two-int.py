def roman2int(roman):
   romans_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
   conversion = 0
   for index, letter in enumerate(roman):
      if index + 1 < len(roman):
         if romans_values[str.upper(roman[index + 1])] > romans_values[str.upper(letter)]:
            conversion = conversion - romans_values[f"{str.upper(letter)}"]
         else:
            conversion = conversion + romans_values[f"{str.upper(letter)}"]
      else:
         conversion = conversion + romans_values[f"{str.upper(letter)}"]
   return conversion
          

roman = str(input("[+] ENTER THE DESIRED ROMAN NUMBER: "))
conversion = roman2int(list(roman))
print(f"{str.upper(roman)} = {conversion}")