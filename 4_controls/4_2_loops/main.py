# 1. Print first 10 natural numbers using while
# 2. Mutual friends
ashvik_friends = ["Ashish", "Arabh", "Arnav", "Pukar"]
lami_friends = ["Uniq", "Avinash", "Pukar" , "Binod"]

for af in ashvik_friends:
  for lf in lami_friends:
    if (af == lf):
      print("Mutual friend found:", af)