import time
t_start = t_current = t_last = time.time()

#range of sqrt(n) to be checked.
START = 10000000000
END   = 99999999999


file = open("output20x.txt", "w")
file.write("t_start:" + str(t_start) + "\n" )
file.write("START:" + str(START) + "\n" )
file.write("END:" + str(END) + "\n" )

i = START
counter = 0

while i <= END:
    counter = counter + 1 #Simple counter to control the printing of intermediate messages

    #Approach 1:
    #sq = i * i
    #print(sq)
    #HUGE BUG IN PYTHON: ( 19421687843317421649 / 10 ) % 10 GIVES 8 !
    #Therefor sq10 was being miss-calculated during higher digit number processing.
    #sq1 = sq % 10
    #sq2 = int(sq / 10) % 10
    #sq3 = int(sq / 100) % 10
    #sq4 = int(sq / 1000) % 10
    #sq5 = int(sq / 10000) % 10
    #sq6 = int(sq / 100000) % 10
    #sq7 = int(sq / 1000000) % 10
    #sq8 = int(sq / 10000000) % 10
    #sq9 = int(sq / 100000000) % 10
    #sq10= int(sq / 1000000000) % 10
    #sq11= int(sq / 10000000000) % 10

    #approach 2:
    #sq = "000000000000000000000000000" + str( i * i ) #padding extra zeros to suppress higher digit extraction error.
    #sq1 = int( sq[-1] )
    #sq2 = int( sq[-2] )
    #sq3 = int( sq[-3] )
    #sq4 = int( sq[-4] )
    #sq5 = int( sq[-5] )
    #sq6 = int( sq[-6] )
    #sq7 = int( sq[-7] )
    #sq8 = int( sq[-8] )
    #sq9 = int( sq[-9] )
    #sq10 = int( sq[-10] )
    #sq11 = int( sq[-11] )
    #sq12 = int( sq[-12] )

    #approach 3:
    sq = i * i
    sq1 = sq % 10
    sq2 = sq // 10 % 10
    sq3 = sq // 100 % 10
    sq4 = sq // 1000 % 10
    sq5 = sq // 10000 % 10
    sq6 = sq // 100000 % 10
    sq7 = sq // 1000000 % 10
    sq8 = sq // 10000000 % 10
    sq9 = sq // 100000000 % 10
    sq10= sq // 1000000000 % 10
    sq11= sq // 10000000000 % 10
    sq12= sq // 100000000000 % 10

    #n = 10000 * ( sq1 * 1000 + sq2 * 100 + sq3 * 10 + sq4 ) + i #Forumulae for 8 digit number.
    #
    
    #n = 100000 * ( sq1 * 10000 + sq2 * 1000 + sq3 * 100 + sq4 * 10 + sq5 ) + i #Forumulae for 10 digit number.
    #Wow!  4270981082
    
    #n = 1000000 * ( sq1*100000 + sq2 * 10000 + sq3 * 1000 + sq4 * 100 + sq5 * 10 + sq6) + i #Forumulae for 12 digit number.
    #Wow!  465454256742
    #Wow!  692153612536
    
    #n = 10000000 * ( sq1*1000000 +sq2*100000 +sq3*10000 +sq4*1000 +sq5*100 +sq6*10 +sq7 ) + i #Forumulae for 14 digit number.
    #
    
    #n = 100000000 * ( sq1*1000000 +sq2*100000 +sq3*10000 +sq4*1000 +sq5*100 +sq6*10 +sq7 ) + i #Forumulae for 15 digit number.
    #Wow! 182921919071841
    #Wow! 655785969669834
    
    #n = 100000000 * ( sq1*10000000 +sq2*1000000 +sq3*100000 +sq4*10000 +sq5*1000 +sq6*100 +sq7*10 +sq8 ) + i #Forumulae for 16 digit number.
    #No Result
    
    #n = 1000000000 * ( sq1*10000000 +sq2*1000000 +sq3*100000 +sq4*10000 +sq5*1000 +sq6*100 +sq7*10 +sq8 ) + i #Forumulae for 17 digit number.
    #No Result

    #n = 1000000000 * ( sq1*100000000 + sq2*10000000 + sq3*1000000 + sq4*100000 + sq5*10000 + sq6*1000 + sq7*100 + sq8*10 + sq9 ) + i #Forumulae for 18 digit number.
    #Wow! 650700037578750084
    #Run-time 5967.29 sec.

    #n = 10000000000 * ( sq1*100000000 +sq2*10000000 +sq3*1000000 +sq4*100000 +sq5*10000 +sq6*1000 +sq7*100 +sq8*10 +sq9 ) + i #Forumulae for 19 digit number.
    
    #n = 10000000000 * ( sq1*1000000000 +sq2*100000000 +sq3*10000000 +sq4*1000000 +sq5*100000 +sq6*10000 +sq7*1000 +sq8*100 +sq9*10 +sq10 ) + i #Forumulae for 20 digit number.

    n = 100000000000 * ( sq1*1000000000 +sq2*100000000 +sq3*10000000 +sq4*1000000 + sq5*100000 + sq6*10000 + sq7*1000 + sq8*100 + sq9*10 + sq10 ) + i #Forumulae for 21 digit number.

    #n = 100000000000 * ( sq1*10000000000 +sq2*1000000000 +sq3*100000000 +sq4*10000000 + sq5*1000000 + sq6*100000 + sq7*10000 + sq8*1000 + sq9*100 + sq10*10 + sq11 ) + i #Forumulae for 22 digit number.

    m = n * n

    #String check.
    n_Str = str(n)[::-1]
    m_Str = str(m)

    if n_Str in m_Str:
        msg = "Wow! " + str(n) + "\n"
        print (msg)
        file.write (msg)

        t_delta = t_current - t_last
        msg = "n:" + str(n) + ",n^2:" + str(m) + ",n_inv:" + n_Str + "-Time: " + str(t_delta) + "\n"
        print (msg)
        file.write (msg)

    if counter == 1000001:
        counter = 0 #Reset the counter.
        t_current = time.time()
        t_delta = t_current - t_last
        t_last = t_current
        
        msg = "n:" + str(n) + ",n^2:" + str(m) + ",n_inv:" + n_Str + "-Time: " + str(t_delta) + "\n"
        #Printing to screen has considerable impact on performance of the program. ~30% extra when done every 100001 iteration.
        print (msg) 
        file.write (msg)

    #msg = "n:" + str(n) + ",n^2:" + str(m) + ",n_inv:" + n_Str + "-Time: " + str(t_delta) + "\n"
    #print (msg)
        
    #While loop control.
    i = i + 1

t_current = time.time()
file.write("t_current:" + str(t_current) + "\n" )
file.write(str(END - START) + " n checked in " + str(t_current - t_start) + " sec." + "\n" )
file.close()
