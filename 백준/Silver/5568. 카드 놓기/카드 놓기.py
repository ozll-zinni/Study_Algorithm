import sys
n = int(input())
k = int(input())
cards = [sys.stdin.readline().strip() for _ in range(n)]

card_list = []

def pick(result, n, picked):
    if n == k:
        if result not in card_list:
            card_list.append(result)
        return

    for card_idx in range(len(cards)):
        if card_idx not in picked:
            picked.append(card_idx)
            new_result = result + cards[card_idx]
            pick(new_result, n+1, picked)
            picked.pop()


pick("", 0, [])
print(len(card_list))