
survey = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'y', 'y', 'a']

food = {
        '마파두부': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'y', 'y', 'a'],
        '탕수육': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'y', 'y', 'a']
}


for i in food.values():
        score = 0
        cnt = 0
        for j in range(10):
                score += 0.1**(j+1)
                if(survey[j] == i[j]):
                        cnt += score
                print(score, cnt)
        print()