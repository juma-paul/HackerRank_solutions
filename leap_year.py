def leap_year(year) -> bool:
  """
  A function to determine if a given year is a leap year.

  Params:
    year(int): the year that the user inputs.
  
  Returns:
      bool: True or False.
  """
  
  leap = False
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap = True
      else:
        leap = False
    else:
      leap = True
  else:
    leap = False

  return leap

def main():
  """
  A main method for testing the function leap_year.
  """
  
  year = int(input("Enter a year, to determine if it's a leap year or not: "))
  res = leap_year(year)
  if res == True:
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is NOT a leap year.")

if __name__ == "__main__":
  main()
    
