#Øving 10

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
    
    def getanswer(self):
        return self.answers[int(self.correct)]
        
    def checkans(self,ans): #Oppgave e sjekk korrekt svar
        return ans == self.correct 
        
        
        
    def ask(self,Data):
        print(self,"\n")

        Output = "\n"
        for name in Data:
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
                    player = Data[name]
                    player.Increment()
                    Output += f"{name}: Correct\n"
            else:
                Output += f"{name}: Incorrect\n"
        
        print("\n")
        print(f'Correct answer: {self.getanswer()}')
        print(Output)


class MultipleChoice:
    def __init__(self,Data):
        self.Questions = list() #list of questions
        self.Data = Data #Dictionary with player objects

    def append_question(self,question, answers, correct):
        self.Questions.append(Flervalg(question,answers,correct))
        return


    def start(self):
        for v in self.Questions:
            v.ask(self.Data)

        highest = 0
        winners = []
        for name in self.Data:
            player = self.Data[name]
            if player.score > highest:
                highest = player.score
                winners = [name]
                
            elif player.score == highest:
                winners.append(name)
            

        if len(winners) == 1:
            winner = winners[0]
            player = self.Data[winner]
            print("The winner is:")
            print(f"{winner} scored {player.score}/{len(self.Questions)}")
        
        else:
            print("Draw between the winners:")
            for winner in winners:
                player = self.Data[winner]
                print(f"{winner} scored {player.score}/{len(self.Questions)}")

        return



class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def Increment(self):
        self.score+=1





if __name__ == "__main__": #only run code underneath if this script is called
    antall = int(input("How many players will be in the game: "))
    Score = dict()
    for i in range(antall):
        name = input(f"What is your name player{i+1}: ")
        Score[name] = Player(name) #Dictionary with player objects
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




            

        




