from student import Questions

exams = [
    "1. who is the president of ghana ?\n a.kuffour\n b.kwame\n c.Nana Addo\n\n", 
            
    "\n2. who is shatta wale ?\n a.musician\n b.rapper\n c.president\n\n", 
          
    "\n3. who is kwabena kwabena ?\n a. boxer\n b.highlife\n c.dancehall\n\n"
]

questions = [
    Questions(exams[0],"c"),
    Questions(exams[1],"a" ),
    Questions(exams[2],"b")
]

def solution(questions):
    score=0
    for idea in questions :
        ans = input(idea.number)
        if ans == idea.answer :
            score = score + 1
    if score >=2 :
        print("you scored " + str(score) + "/" + str(len(exams)) + " excellent")
    else :
        print("you scored " + str(score) + "/" + str(len(exams)) + " you failed")
    

         


        
        
solution(questions)






