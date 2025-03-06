def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    lastL, lastR = '*', '#'
    answer = ''

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            lastL = num
        elif num in [3, 6, 9]: 
            answer += 'R'
            lastR = num
        else:  
            
            cur_pos = keypad[num]
            left_pos = keypad[lastL]
            right_pos = keypad[lastR]

            distanceL = abs(cur_pos[0] - left_pos[0]) + abs(cur_pos[1] - left_pos[1])
            distanceR = abs(cur_pos[0] - right_pos[0]) + abs(cur_pos[1] - right_pos[1])

            if distanceL < distanceR:
                answer += 'L'
                lastL = num
            elif distanceL > distanceR:
                answer += 'R'
                lastR = num
            else: 
                if hand == 'right':
                    answer += 'R'
                    lastR = num
                else:
                    answer += 'L'
                    lastL = num

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand)) 
