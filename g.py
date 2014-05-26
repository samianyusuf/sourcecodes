def petro():
   
    x=float (raw_input("Enter POS: "))
    y=float (raw_input("Enter safedrops: "))
    z=float (raw_input("Enter payout: "))

    
    total=x+y+z
    print "Your total is: " ,total

    v=float( raw_input("NOW ENTER GRAND TOTAL SALE: "))

    SO=total-v

    if (v>total):
        print "You are short: ",SO

    else:
        print("You are over: "),SO
    
