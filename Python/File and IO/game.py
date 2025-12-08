n = int(input("Enter the number : "))

with open("hi-score.txt","r") as f:
    data = f.read().strip()
    if(data==""):
        score = 0
    else:
        score = int(data)
    if(n>score):
        with open("hi-score.txt","w") as f:
            print("Congratulation New Highest score is ",n)
            f.write(str(n))
        
    else: 
        print("previous Highest score is ",score)