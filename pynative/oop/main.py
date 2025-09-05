class FileName:
  count = 0
  def __init__(self, file_name = None):
    if file_name is None:
      FileName.count = FileName.count + 1
      self.file_name = f"Untitled-{FileName.count}"
    else:
      self.file_name = file_name
  
  @staticmethod
  def delete_file():
    FileName.count = FileName.count - 1

oop = FileName()
python = FileName("main.py")
java = FileName()
FileName.delete_file()
c = FileName()
print(oop.file_name)
print(python.file_name)
print(java.file_name)
print(c.file_name)