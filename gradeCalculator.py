def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    score = float(input("Enter score:"))
    float_score=score
    try: 
        if float_score < 0.0 or float_score> 1.0: 
            print("Bad score")
        elif float_score >= 0.9:
            print("A")
        elif float_score >= 0.8:
            print("B")
        elif float_score >= 0.7:
            print("C")
        elif float_score >= 0.6:
            print("D")
        elif float_score < 0.6:
            print("F")
    except:
        print("Please enter a number 0.0 - 1.0")    

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()