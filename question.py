class Question:
  def __init__(self, title, content, opt1, opt2, opt3, opt4, correct_i):
    self.title = title
    self.content = content
    self.opt1 = opt1
    self.opt2 = opt2
    self.opt3 = opt3
    self.opt4 = opt4
    self.correct_i = correct_i

  def __str__(self):
    return self.title + " " + self.content + " " + self.opt1 + " " + self.opt2 + " " + self.opt3 + " " + self.opt4 + " vi tri dung: " + str(self.correct_i)
