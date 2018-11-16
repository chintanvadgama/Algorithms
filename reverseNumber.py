
def reverser_number(number):
  if isinstance(number, float):
      decimal,fraction = str(abs(number)).split('.')
      decimal = int(decimal)
      fraction = int(fraction)
      rev_decimal = rev_helper(decimal)
      rev_fraction = rev_helper(fraction)
      if number < 0:
        reversed_num = '-' + str(rev_decimal) + '.' + str(rev_fraction)
      else:
        reversed_num = str(rev_decimal) + '.' + str(rev_fraction)
  else:
      decimal = abs(number)
      reversed_num = rev_helper(decimal)
      if number < 0:
        reversed_num = '-' + str(reversed_num)
      else:
        reversed_num = str(reversed_num)
  return reversed_num



def rev_helper(number):
  reverse = 0
  while number > 0:
    rem = number % 10
    reverse = (reverse * 10) + rem
    number = number // 10
  return reverse

print(reverser_number(562981))
print(reverser_number(-562981))
print(reverser_number(123.12))
print(reverser_number(-123.12))
print(reverser_number(123.00))

