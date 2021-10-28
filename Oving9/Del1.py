#Øving 9

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
    
    def getanswer(self): #Oppgave e sjekk korrekt svar
        return self.answers[int(self.correct)]
        
    def checkans(self,ans): 
        return ans == self.correct 
        
        
        
    def ask(self,Score):
        print(self,"\n")

        Output = "\n"

        for name in Score:
            while True:
                try:
                    ans = int(input(f"Select a choice {name}: "))
                    if ans >= 0 and ans <= len(self.answers)-1:
                        break
                    else:
                        print('Your option is not valid')
                except ValueError: 
                    print('Your answer is not valid')
        
            ans = str(ans)
            if self.checkans(ans):
                    Score[name] += 1
                    Output += f"{name}: Correct\n"
            else:
                Output += f"{name}: Incorrect\n"
        
        print("\n")
        print(f'Correct answer: {self.getanswer()}')
        print(Output)


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



        highest = 0
        winners = []
        for name in self.Score:
            if self.Score[name] > highest:
                highest = self.Score[name]
                winners = [name]
                
            elif self.Score[name] == highest:
                winners.append(name)
            

        if len(winners) == 1:
            winner = winners[0]
            print("The winner is:")
            print(f"{winner} scored {self.Score[winner]}/{len(self.Questions)}")
        
        else:
            print("Draw between the winners:")
            for winner in winners:
                print(f"{winner} scored {self.Score[winner]}/{len(self.Questions)}")

        return



if __name__ == "__main__": #only run code underneath if this script is called
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


    print("\n")
    Test.start()




            

        




