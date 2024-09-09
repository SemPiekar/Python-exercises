import random

bingo_card = []
bingo_card_size = 4
bingo_number_total = bingo_card_size ** 2
numbers = list(range(1, 100))
random.shuffle(numbers)
bingo_numbers = numbers[:bingo_number_total]

for line in range(bingo_card_size):
  bingo_row = []
  for column in range(bingo_card_size):
      bingo_row.append(bingo_numbers.pop())
      bingo_card.append(bingo_row)
print(bingo_card)

# Hier loop ik vast