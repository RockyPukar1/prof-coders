"""
1) load, grayscale, show, save
2) load, grayscale, user_input(show or save),
  if show
    show and destroy
  elif save
    input file name and save
"""

image = imread(<file location>)
check if image loaded
gray_image = cvtColor(image, cv.BGR2GRAY)
uc = input("Enter y for showing and n for saving")
if uc == "y":
  imshow("window name", gray_image)
  wait
  destroy
elif uc == "n":
  uc = input("Enter file name location")
  cv.imwrite(uc, gray_image)
else:
  print("Wrong input")
imshow("window name", gray_image)
wait
destroy
cv.imwrite("phase1/hi.jpeg", gray_image)
