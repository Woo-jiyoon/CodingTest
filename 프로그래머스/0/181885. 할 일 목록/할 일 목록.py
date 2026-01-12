def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        # i번째 일이 아직 끝나지 않았다면(False라면)
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer