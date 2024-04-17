# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:55:14 2023

@author: Rebel
"""



# importing libraries :-
import sys


# Introduction of Quiz :-
print("\nThe Ultimate Quiz")
print("\nWelcome to the Quiz!!!\n")

# To start the Quiz :-
start = input("Want to start the Quiz?\nYES or NO\n") 
if start.lower() != "yes":
    print("\nQuiz Ended.\n\n")
    sys.exit()

# General Instructions of Quiz :-
print("\n\nGENERAL INSTRUCTIONS OF QUIZ:-")
print("\n1: There are 3 Levels of Quiz:- \n  (i)   Easy Level \n  (ii)  Moderate Level \n  (iii) Difficult Level")
print("\n2: If you do not get qualifying marks in Each Level,then you will not go further in next Level.")
print("\n3: There are Separate qualifying marks for Each Level.")
print("\n4: There will be separate instructions before every Level of quiz,Please read it carefully.")
print("\n5: After completion of 3-Tier Quiz;You will be awarded with a 'Certificate'.\n\n")

# To start for Easy Level Quiz :-
start = input("\nLog-in for the Easy Level of Quiz ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.\n\n")
    sys.exit()

# Instructions for Easy Level :-
print("\n\nInstructions for Easy Level :-")
print("\n1: There are total 12 questions.")
print("\n2: Every question is Compulsory;Thus you cannot SKIP any question.")
print("\n3: There is NO Negative marking.")
print("\n4: Every question carries 1 mark.")
print("\n5: To Qualify for Moderate Level you have to get 7 marks or get 7 questions correct.")
print("\n6: If you don't get Qualifying marks , you will not Qualify for next Level of Quiz.")
print("\n7: For every question there are 4 options i.e. (a),(b),(c),(d).")
print("\n8: You have to select only correct option to answer the question i.e. a,b,c,d")
print("\n          !!!Best of Luck!!!\n\n")

# Log-in for Easy Level Quiz :-
start = input("\nReady for Easy Level ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n\n")
    sys.exit()

# Questions of Easy Level Quiz:-
score = 0
# Q 1   
a = input("\n\nQ.1. For which 'FRUIT' Nagpur city is known for? \n(a) Apple \n(b) Orange \n(c) Banana \n(d) Figs \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("orange"):  
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
    print("Ooops!!! you got a wrong answer.")
    
# Q 2
a = input("\nQ.2. Who is the current 'PRESIDENT' of India? \n(a) Ram Nath Kovind \n(b) Jagdeep Dhankhar \n(c) Droupadi Murmu \n(d) Pranab Mukherjee \n Your answer is: ")
if a.lower() == ("c") or  a.lower() == ("droupadi murmu"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 3
a = input("\nQ.3. Which is the 'Largest' animal on earth? \n(a) Blue Whale \n(b) Giraffe \n(c) Ostrich \n(d) Elephant \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("blue whale"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 4
a = input("\nQ.4. Longest river in the world? \n(a) Godavari \n(b) Amazon \n(c) Yangtze \n(d) Nile \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("nile"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")
     
# Q 5
a = input("\nQ.5. Which colour is not present in Rainbow? \n(a) Red \n(b) Orange \n(c) Pink \n(d) Indigo \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("pink"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 6
a = input("\nQ.6. In which year India got Independence? \n(a) 1947 \n(b) 1946 \n(c) 1944 \n(d) 1948 \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("1947"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 7
a = input("\nQ.7. National bird of India is? \n(a) Kiwi \n(b) Parrots \n(c) Owl \n(d) Peacock \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("peacock"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 8
a = input("\nQ.8. If Royal is @\nMonarch is ^\nXinzi is !\nThen what will be the code for Royal Xinzi? \n(a) ^@ \n(b) !@ \n(c) @! \n(d) @^ \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("@!"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 9
a = input("\nQ.9. What is the opposite of 'Cheap'? \n(a) Expensive \n(b) Inexpensive \n(c) Low \n(d) Massive \n Your answer is: ")
if a.lower() == ("a") or  a.lower() == ("expensive"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 10
a = input("\nQ.10. Name the village of which the cartoon character 'BHEEM' is associated? \n(a) Kanpur \n(b) Dholakpur \n(c) Furfuri Nagar \n(d) Jaunpur \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("dholakpur"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 11
a = input("\nQ.11. If 5+6=11 Then 8+7= ? \n(a) 12 \n(b) 15 \n(c) 21 \n(d) 11 \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("15"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")

# Q 12
a = input("\nQ.12. How many sides does 'Pentagon' have? \n(a) Five \n(b) Four \n(c) Eight \n(d) Ten \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("five"): 
    print("Hurray!!! You got a correct answer.")
    score += 1
else:
     print("Ooops!!! You got a wrong answer.")
     
# Result of Easy Level :-
result = input("\nDo you want to see your result?\nYES or NO\n")
if result.lower() != "yes":
    sys.exit()

total_score = 12  
percentage = ((score / (total_score)) * 100)
print("\n\n\nTotal Score: " + str(score))
print("\nYou got: " + str(percentage) + "%")

# To Qualify for moderate level :-
if score >= 7 :
    print("\nCongratulations you are qualified for Next level")
else :
    print("\nOoops!!! You are not Qualified for Next Level.")
    print("\nBetter Luck Next Time.")
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n")
    sys.exit()


# To start Moderate level :-
start = input("\n\nLog-in for the Moderate Level of Quiz ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\n\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.\n\n")
    sys.exit()

# Instructions for Moderate Level :-
print("\n\nInstructions for Moderate Level :-")
print("\n1: There are total 10 questions.")
print("\n2: Every question is Compulsory;Thus you cannot SKIP any question.")
print("\n3: There is a Negative marking of -0.5 for each question.")
print("\n4: Every question carries 2 marks.")
print("\n5: To Qualify for Difficult Level you have to get 10 marks or get 6 questions correct.")
print("\n6: If you don't get Qualifying marks , you will not Qualify for next Level of Quiz.")
print("\n7: For every question there are 4 options i.e. (a),(b),(c),(d).")
print("\n8: You have to select only correct option to answer the question i.e. a,b,c,d")
print("\n          !!!Best of Luck!!!\n\n")

# Log-in for Moderate Level Quiz :-
start = input("\n\nReady for Moderate Level ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\n\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n\n")
    sys.exit()

# Questions of Moderate Level Quiz:-
score = 0
# Q 1 
a = input("\n\nQ.1. Which animal is known as the 'SHIP OF THE DESERT'? \n(a) Sand Cat \n(b) Scorpion \n(c) Sidewinder Snake \n(d) Camel \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("camel"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 2 
a = input("\nQ.2. Name the country known as 'Land of the Rising Sun'? \n(a) Japan \n(b) Korea \n(c) China \n(d) Singapore \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("japan"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5

# Q 3
a = input("\nQ.3. Which city is known as 'City of Joy'? \n(a) Delhi \n(b) Jaipur \n(c) Kolkata \n(d) Mizoram \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("kolkata"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5

# Q 4
a = input("\nQ.4. Who was the 3rd son of Kunti in the epic 'MAHABHARATHA'? \n(a) Duryodhana \n(b) Arjun \n(c) Dushasana \n(d) Bhima \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("arjun"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5

# Q 5
a = input("\nQ.5. The Kamakhya Devi temple is located in which city ? \n(a) Guwahati \n(b) Kohima \n(c) Imphal \n(d) Agartala \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("guwahati"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5
     
# Q 6
a = input("\nQ.6. Which of this is not an alias of 'Lord Krishna'? \n(a) Hrishikesh \n(b) Matsya \n(c) Sita \n(d) Varaha \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("sita"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5 

# Q 7
a = input("\nQ.7. Which word does not belong with the others ? \n(a) Tulip \n(b) Rose \n(c) Bud \n(d) Daisy \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("bud"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5 
     
# Q 8
a = input("\nQ.8. If SUMMER is coded as RUNNER then the code for WINTER is ? \n(a) SUITER \n(b) VIOUER \n(c) WALKER \n(d) SUFFER \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("viouer"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5 

# Q 9
a = input("\nQ.9. Branch in philosophy that is concerned with beauty and art is ? \n(a) Epistermology \n(b) Ethics \n(c) Metaphysics \n(d) Aesthetics \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("aesthetics"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5 
     
# Q 10
a = input("\nQ.10. Who certifies the money bill in India ? \n(a) President \n(b) Vice President \n(c) Chairman of Rajya Sabha \n(d) Speaker of Lok Sabha \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("speaker of lok sabha"): 
    print("Hurray!!! You got a correct answer.")
    score += 2
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 0.5 
    
# Result of Moderate Level :-
result = input("\nDo you want to see your result?\nYES or NO\n")
if result.lower() != "yes":
    sys.exit()

total_score = 20  
percentage = ((score / (total_score)) * 100)
print("\n\n\nTotal Score: " + str(score))
print("\nYou got: " + str(percentage) + "%")

# To qualify for difficult level :-
if score >= 10:
    print("\nCongratulations you are qualified for Next level")
else :
    print("\nOoops!!! You are not Qualified for Next Level.")
    print("\nBetter Luck Next Time.")
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n")
    sys.exit()


# To start Difficult level :-
start = input("\nLog-in for the Difficult Level of Quiz ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.\n")
    sys.exit()

# Instructions for Difficult Level :-
print("\n\nInstructions for Difficult Level :-")
print("\n1: There are total 8 questions.")
print("\n2: Every question is Compulsory;Thus you cannot SKIP any question.")
print("\n3: There is a Negative marking of -1 for each question.")
print("\n4: Every question carries 4 marks.")
print("\n5: To Pass the Difficult Level you have to get 12 marks or get 4 questions correct.")
print("\n6: If you don't get Qualifying marks , you will not be considered as Pass.")
print("\n7: For every question there are 4 options i.e. (a),(b),(c),(d).")
print("\n8: You have to select only correct option to answer the question i.e. a,b,c,d")
print("\n          !!!Best of Luck!!!\n")

# Log-in for Difficult Level Quiz :-
start = input("\n\nReady for Difficult Level ?\nYES or NO\n") 
if start.lower() != "yes":
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n")
    sys.exit()

# Questions of Difficult Level Quiz:-
score = 0
# Q 1 
a = input("\nQ.1. A column is a ______ representation of data? \n(a) Diagonal \n(b) Vertical \n(c) Horizontal \n(d) Top \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("vertical"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 2
a = input("\nQ.2. Choose the correct components of data science ? \n(a) Domain Expertise \n(b) Data Engineering \n(c) Advanced Computing \n(d) All of the above \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("all of the above"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 3
a = input("\nQ.3. Which of the following is not a part of the data science process ? \n(a) Communication Building \n(b) Operationalize \n(c) Model Planning \n(d) Discovery \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("communication building"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 4
a = input("\nQ.4. GRAVITY : Pull :: MAGNETISM :?  ? \n(a) Repulsion \n(b) Separation \n(c) Attraction \n(d) Push \n Your answer is: ")
if a.lower() == ("c") or a.lower() == ("attraction"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 5
a = input("\nQ.5. In a certain code '256' is 'you are good' ,'637' is 'we are bad' ,'358' is 'good and bad';then which number represents 'and' in that code? \n(a) 2 \n(b) 5 \n(c) 6 \n(d) 8 \n Your answer is: ")
if a.lower() == ("d") or a.lower() == ("8"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 6
a = input("\nQ.6. Which is known as the 'HEART' of an atomic power plant? \n(a) Reactor \n(b) Steamer \n(c) Turbine \n(d) Coolant \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("reactor"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 7
a = input("\nQ.7. Which is the largest island in the world ? \n(a) Greenland \n(b) New Zealand \n(c) Iceland \n(d) Finland \n Your answer is: ")
if a.lower() == ("a") or a.lower() == ("greenland"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1

# Q 8
a = input("\nQ.8. Which of the following python library is used for 'Web Development' ? \n(a) Vue \n(b) Django \n(c) Angular \n(d) jQuery \n Your answer is: ")
if a.lower() == ("b") or a.lower() == ("django"): 
    print("Hurray!!! You got a correct answer.")
    score += 4
else:
     print("Ooops!!! You got a wrong answer.")
     score -= 1


# Result of Difficult Level :-
result = input("\nDo you want to see your result?\nYES or NO\n")
if result.lower() != "yes":
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.\n")
    print("\n!!!Thank You!!!\n")
    sys.exit()

total_score = 32 
percentage = ((score / (total_score)) * 100)
print("\n\nTotal Score: " + str(score))
print("\nYou got: " + str(percentage) + "%")

# Pass or Fail :-
if score >= 12:
    print("\nCongratulations you have PASSED the Quiz.")
else :
    print("\nOoops!!! You FAILED the Quiz.")
    print("\nBetter Luck Next Time.")
    print("\nQuiz Ended.")
    print("\nCome Back Later with Lots of Knowledge.")
    print("\n!!!Thank You!!!\n")
    sys.exit()


# To get a certificate :-
start = input("\n\nDo you want your Certificate ?\nYES or NO\n") 
if start.lower() == "yes":
    print("\nINSTRUCTIONS FOR CERTIFICATE:- ")
    print("1: Please Write your name.\n\n")
else:
    print("\n!!!Thank You!!!\n")
    sys.exit()
    
print("\n\n\n\n                    CERTIFICATE")                     # 20 space required
print("----------------Of Excellence Award----------------")   # 15 - required both sides
print("\n                 Proudly Awarded to")                  # 17 space required
print(input("" "\n"))      # "" :- to write name and "\n" :- to get output below input.
print("\n              Has got " + str(percentage) + "%" + " " + "and Successfully completed 3-Tier Quiz competition known as 'THE ULTIMATE QUIZ'.We Acknowledge your efforts,keep participating.")
print("\n\n\nMr.AAYUSH                          Mr.AAYUSH")    # 26 space required
print("Quiz Developer                     Event Coordinator")  # 21 space required


#---------END--------#