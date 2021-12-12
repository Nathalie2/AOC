# -*- coding: utf-8 -*-
import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

numbers = [int(nr) for nr in lines[0].split(',')]
card_length = 6
nr_of_cards = len(lines[1:])//card_length

cards = [[[[int(el),None] for el in re.split(r'[ ]+',row.strip()) ] for row in card] for card in [lines[i+1:i+card_length] for i in range(1,nr_of_cards*card_length,card_length)]]

def mark_card(card, draw):
    for row in card:
        for el in row:
            if el[0] == draw:
                el[1] = True
                return

def check_cards_first_win(card, draw):
    for row in card:
        if all([x[-1] for x in row]):
            unmarked =[[el[0] for el  in row if el[-1]!=True] for row in card]
            unmarked_sum = sum([item for sublist in unmarked for item in sublist])
            print(unmarked_sum*draw)
            return True
    t_card = [list(x) for x in zip(*card)]
    for col in t_card:
        if all([x[-1] for x in col]):
            unmarked =[[el[0] for el  in col if el[-1]!=True] for col in card]
            unmarked_sum = sum([item for sublist in unmarked for item in sublist])
            print(unmarked_sum*draw)
            return True

def check_cards_last_win(card, draw, last):
    for row in card:
        if all([x[-1] for x in row]):
            unmarked =[[el[0] for el  in row if el[-1]!=True] for row in card]
            unmarked_sum = sum([item for sublist in unmarked for item in sublist])
            if last== True:
                print(unmarked_sum*draw)
            return 'done'
    t_card = [list(x) for x in zip(*card)]
    for col in t_card:
        if all([x[-1] for x in col]):
            unmarked =[[el[0] for el  in col if el[-1]!=True] for col in card]
            unmarked_sum = sum([item for sublist in unmarked for item in sublist])
            if last == True:
                print(unmarked_sum*draw)
            return 'done'

def part1(cards, numbers):
    for draw in numbers:
        for card in cards:
            mark_card(card, draw)
            if check_cards_first_win(card,draw):
                return

def part2(cards, numbers, cards_state, last):
    for draw in numbers:
        for i_c in range(len(cards)):
            if sum(card is None for card in cards_state) ==1:
                last=True
            if cards_state[i_c]!= 'done':
                mark_card(cards[i_c], draw)
                cards_state[i_c]=check_cards_last_win(cards[i_c], draw, last)

part1(cards,numbers)
cards_state = [None for x in cards]
part2(cards, numbers, cards_state, False)




