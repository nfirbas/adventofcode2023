def readFile():
    f = open("./input.txt", "r")
    return [line.rstrip('\n') for line in f]


def first_star(cards):
    sum = 0
    for card in cards:
        nums = card.split(": ")[1].split(" | ")[0].split(" ")
        wining_nums = card.split(": ")[1].split(" | ")[1].split(" ")
        nums_dic = {}
        counter = 0
        
        for n in nums:
            if n.isdigit():
                counter += 1
                nums_dic[int(n)] = 1
        for n in wining_nums:
            if n.isdigit():
                nums_dic.pop(int(n), None)

        if len(nums_dic) < counter:
            sum += pow(2,counter-1-len(nums_dic))
    print(sum)

def remove_dict(dictionary, number):
    return { key: dictionary[key] for key in dictionary if key <= number }

def second_star(cards):
    cards_won = {}
    for i in range(len(cards)):
        if i not in cards_won: cards_won[i] = 1
        else : cards_won[i]+=1
        
        nums = cards[i].split(": ")[1].split(" | ")[0].split(" ")
        wining_nums = cards[i].split(": ")[1].split(" | ")[1].split(" ")
        nums_dic = {}
        counter = 0
        
        for n in nums:
            if n.isdigit():
                counter += 1
                nums_dic[int(n)] = 1
        for n in wining_nums:
            if n.isdigit():
                nums_dic.pop(int(n), None)

        wins = counter-len(nums_dic)
        for j in range(i+1,i+1+wins):
            if j not in cards_won:
                cards_won[j] = 0
            cards_won[j] += cards_won[i]
        
    
    print(sum(remove_dict(cards_won, len(cards)-1).values()))
        


if __name__ == "__main__":
    cards = readFile()

    first_star(cards)
    second_star(cards)