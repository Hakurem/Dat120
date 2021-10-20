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
        
        
        
    def ask(self,Score):
        print(self,"\n")



        for name in Score:
            while True:
                try:
                    ans = int(input(f"Select a choice {name}: "))
                    if ans >= 0 and ans <= len(self.answers):
                        break
                    else:
                        print('Your option is not valid')
                except ValueError: 
                    print('Your answer is not valid')
        
            ans = str(ans)
            if self.checkans(ans) and name in Score:
                    Score[name] += 1
        print("\n")


class MultipleChoice:
    def __init__(self,Score):
        self.Questions = list() #list of questions
        self.Score = Score

    def append_question(self,question, answers, correct):
        self.Questions.append(Flervalg(question,answers,correct))
        return


    def start(self):
        for v in self.Questions:
            v.ask(self.Score)

        print('The result is:')
        for name in self.Score:
            print(f"{name} score was {self.Score[name]}/{len(self.Questions)}")
        return





antall = int(input("How many players will be in the game: "))
Score = dict()
for i in range(antall):
    name = input(f"What is your name player{i+1}: ")
    Score[name] = 0
Test = MultipleChoice(Score)


with open("sporsmaalsfil.txt","r",encoding = "UTF8") as file:
    for linje in file:
        liste = linje.split(":")
        
        question = liste[0].strip()
        correct = liste[1].strip()

        slice = liste[2].split(",")
        answers = list()
        for element in slice:
            element = element.strip().strip("[]")
            answers.append(element)
        Test.append_question(question,answers,correct)


Test.start()




            

        




