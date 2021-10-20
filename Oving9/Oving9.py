class Flervalg:
    def __init__(self, question,answers,correct):
        self.question = question
        self.answers = answers
        self.correct = correct
        
    def __str__(self):
      output = f"{self.question}\n"
      for i,v in enumerate(self.answers):
          output += f"\n{i}. {v}"
      return output
     
        
    def checkans(self,ans):
        return ans == self.correct 
        
        
    def ask(self):
        print(self)
        while True:
            try:
                ans = int(input("Write the number of the correct choice: "))
                if ans >= 1 and ans <= len(self.answers):
                    break
                else:
                    print('Your option is not valid')
            except ValueError: 
                print('Your answer is not valid')
        
        print("\n")
        return self.checkans(ans)


class MultipleChoice:
    def __init__(self):
        self.Questions = list()
        self.Correct = 0
        self.Antall = 0

    def append_question(self,question, answers, correct):
        self.Questions.append(Flervalg(question,answers,correct))
        return


    def start(self):
        for v in self.Questions:
            self.Correct += v.ask()
        print(f"Your score was {self.Correct}/{self.Antall}")
        return

import pathlib
print(pathlib.Path)
Test = MultipleChoice()
with open("sporsmaalsfil.txt","r",encoding = "UTF8") as file:
    for linje in file:
        liste = linje.split(":")
        for element in liste:
            question = element[0]
            answers = element[1]
            correct = element[2]
            Test.append_question(question,answers,correct)


Test.start()




            

        




