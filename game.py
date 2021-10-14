# -*- coding: utf-8 -*-

import random


'''Game
该demo实现了游戏规则的核心算法

其中卡片为单张添加，未考虑多张卡片一起添加的情形

未考虑并发的影响

'''

class Card:

    def __init__(self, shape=None):
        if shape is None:
            shape = 0
            for _ in range(4):
                ret = random.randint(0, 2)
                shape = shape << 2 | ret
        self.shape = shape 


class Game(object):

    ADD_DENEY = -1
    ADD_SUCCESS = 0
    ADD_FAIL = 1

    def __init__(self, vol=0, col=0):
        self.vol = vol
        self.col = col
        self.pending_cards = [[None] * self.vol for i in range(self.col)]
        self.progress = 0

    def reset(self):
        self.pending_cards = [[None] * self.vol for i in range(self.col)]
        self.progress = 0

    def addCard(self, card=None, w_idx=-1, h_idx=-1):
        if self.progress >= self.vol * self.col:
            return self.ADD_DENEY
        if not card:
            return self.ADD_DENEY
        if not (w_idx >= 0 and w_idx < self.col and h_idx >=0 and h_idx < self.vol):
            return self.ADD_DENEY

        ret = 0
        for i in range(4):
            # down right up left
            p_w_idx = w_idx + i%2 * ((-1) ** (i//2))
            p_h_idx = h_idx + (i+1)%2 * ((-1) ** (i//2))
            # 边界值
            i_val, j_val = 1, 1
            if p_w_idx >= 0 and p_w_idx < self.col and p_h_idx >= 0 and p_h_idx < self.vol:
                w_card = self.pending_cards[p_w_idx][p_h_idx]
                if w_card is not None:
                    j = ((i + 2) % 4) * 2
                    j_val = 0b11 & w_card.shape >> j
                    i_val = 0b11 & card.shape >> (i*2)
                else:
                    i_val = 1
            if i_val + j_val == 2:
                ret |= 1 << i

        if ret == 0b1111:
            self.progress += 1
            self.pending_cards[w_idx][h_idx] = card
            if self.progress == self.vol * self.col:
                print("游戏结束！！！")
            return self.ADD_SUCCESS

        return self.ADD_FAIL


    def deleteCard(self, w_idx=-1, h_idx=-1):
        if w_idx >= 0 and w_idx < self.vol and h_idx >=0 and h_idx < self.col:
            if self.pending_cards[w_idx][h_idx]: 
                self.progress -= 1
                self.pending_cards[w_idx][h_idx] = None


def run():
    vol, col = 3, 5
    g = Game(vol, col)
    for i in range(col):
        for j in range(vol):
            while True:
                card = Card()
                ret = g.addCard(card, i, j)
                if ret == Game.ADD_SUCCESS:
                    break
    g.reset()