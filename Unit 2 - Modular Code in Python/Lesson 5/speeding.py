def caught_speeding(speed,is_birthday):
    small_ticket = False
    big_ticket = False
    if is_birthday==True:
        if speed>=56 and speed<=75:
            small_ticket = True
        if speed>=76:
            big_ticket = True 
        speed = speed-5
    else:
        if speed>=61 and speed<=80:
            small_ticket = True
        if speed>=81:
            big_ticket = True 
        speed = speed-5
    print("Small ticket: "+str(small_ticket))
    print("Big ticket: "+str(big_ticket))

caught_speeding(75,True)