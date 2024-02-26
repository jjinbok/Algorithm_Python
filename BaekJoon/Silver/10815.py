has_card_num = int(input())
has_card = input().split()
all_card_num = int(input())
all_card = input().split()

has_card_set = set(has_card)

ans_card_arr = [1 if card in has_card else 0 for card in all_card]

print(" ".join(map(str, ans_card_arr)))


