def roman2int(roman):
   romansValues = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
   conversion = 0
   for index, letter in enumerate(roman):
      if index + 1 < len(roman):
         if romansValues[str.upper(roman[index + 1])] > romansValues[str.upper(letter)]:
            conversion = conversion - romansValues[f"{str.upper(letter)}"]
         else:
            conversion = conversion + romansValues[f"{str.upper(letter)}"]
      else:
         conversion = conversion + romansValues[f"{str.upper(letter)}"]
   return conversion
          

roman = str(input("Informe o número romano desejado: "))
conversion = roman2int(list(roman))
print(f"{str.upper(roman)} = {conversion}")