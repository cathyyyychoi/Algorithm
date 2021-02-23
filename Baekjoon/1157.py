input_word = input().upper()
word_list = list(set(input_word))
cnt_list = []

for i in word_list:
    cnt = input_word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    idx = cnt_list.index(max(cnt_list))
    print(word_list[idx])
