def solution(new_id):
    # stage 1
    new_id = new_id.lower()

    #stage 2
    answer = ""
    for ch in new_id:
        if ch.isalnum() or ch in "-_.":
            answer += ch

    # stage 3
    while ".." in answer:
        answer.replace('..', ',')

    # stage 4
    if answer[0] == ".":
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]

    # stage 5
    if answer == "":
        answer = "a"

    # stage 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # stage 7
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer

new_id = "abcdefghijklmn.p"	
print(solution(new_id))
