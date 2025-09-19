set_a = {4, 5, 11, 5, 13}
set_b = {5, 11, 16, 17}
set_c = {15, 16, 18}

class SetOperation:
  def find_intersection(self, *arg):
    print(arg)
    match len(arg):
      case 2:
        for i in range(10): # earth (15000)
          star = ""
          for _ in range(i):
            star += " *"
          print(star)
      case 3:
        print("three")

result = SetOperation()
result.find_intersection(set_a, set_b)
# result.find_intersection(set_a, set_b, set_c)
# *
# * *
# * * *