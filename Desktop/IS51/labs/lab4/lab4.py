



"""
this program allows users three tries to guess the correct answer to a question
"what is the capitol of california" answer = Sacramento


set max tries to 3 then we create a loop to iterate them three times
in each iteration we ask the user for an answer and then check to see if it is correct.
if the answer is correct, print "Correct!" and rterminate the program.

if the user could not get the answer correct then print "you have used up all 3 of your chances" and termiate the program


"""

"""
main():
     question = what is the capitol of california 
     answer = sacramento
     ask(question, answer)

ask():
    tries = 0
    loop three times
        increment three tries
        ask user input
        check if user input is equal to answer
        if so print "Correct!" and exit loop
"""

def main():
    question = "What is a capitol of California? \n"
    answer = "Sacramento"
    ask(question, answer)

def ask(question, answer, max_tries = 3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
        if ans != answer:
            print("You used one of your guesses")
    if ans != answer:
            print("game over")


main()
