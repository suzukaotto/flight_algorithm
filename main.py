from random import choice

def fuck_seat():
    is_seat = [False] * 100
    remain_seat = [i for i in range(100)]
    
    for pass_num in range(100):
        seat_num = pass_num
        if (pass_num==0) or (is_seat[pass_num]==True):
            seat_num = choice(remain_seat)
        
        is_seat[seat_num] = True
        remain_seat.remove(seat_num)
    
    return True if seat_num==99 else False, seat_num

count = 100000
success = 0
fail = 0
for i in range(count):
    result = fuck_seat()
    
    if result[0]:
        success += 1
    else:
        fail += 1

print(f"{(count-fail)/1000}% | count={count} | success={success} | fail={fail} | last_pass_seat_num={result[1]}")