# This file will be used in the competition
# Please make sure the following functions are well defined
# MCTS Version 3
# Chen-An Fan

from advance_model import *
from utils import *


class myPlayer(AdvancePlayer):
    counter = 0 #count how many action has this player done
    #grid_color = -1
    #reward = 0
    
    # initialize
    # The following function should not be changed at all
    def __init__(self,_id):
        super().__init__(_id)
        self.counter = 0
        #self.grid_color = -1
        #self.reward = 0
        #self.pt = PlayerTrace(self.id)
    # Each player is given 5 seconds when a new round started
    # If exceeds 5 seconds, all your code will be terminated and 
    # you will receive a timeout warning
    def StartRound(self,game_state):
        
        return None

    # Each player is given 1 second to select next best move
    # If exceeds 5 seconds, all your code will be terminated, 
    # a random action will be selected, and you will receive 
    # a timeout warning
    def SelectMove(self, moves, game_state):
        #move傳進來已經是avaliable move了
        #a copy of the current game state
    
        player_state = game_state.players[self.id]
        #copyGS = copy.deepcopy(game_state)
        #copyPS = copyGS.players[self.id]
        #copyPS = copy.deepcopy(player_state)
        
        opponentId = abs(self.id - 1)
        opponnent_state = game_state.players[opponentId]
        
        myGridState = player_state.grid_state #這是做動作之前的State看此有沒有東西
        #copyGrid = copyPS.grid_state
        myGridScheme = player_state.grid_scheme
        maxReward = 0
        best_move = random.choice(moves) #Randon initial the move
        print("==================new action====================")
        for mid,fid,tgrab in moves:
            move = (mid,fid,tgrab)
            rowIsFull = False
            # Reset the player_state and grid_state to original one before any move
            copyGS = copy.deepcopy(game_state) # A new address
            copyPS = copyGS.players[self.id]   # A new address
           
            preGridState = copy.deepcopy(copyPS.grid_state) #for debug
            #print(preGridState)
            # Try to execute the move outside the main
            copyGS.ExecuteMove(self.id, move) #This will change and update the game state
            score = copyPS.ScoreRound()[0] #this will change the grid_state and the player_state
            bonus = copyPS.EndOfGameScore()
            reward = score + bonus
            print("score = " + str(score))
            print("bonus = " + str(bonus))
            print("reward = " + str(reward))
            afeGridState = copyPS.grid_state
            #print(preGridState)
            print("---")
            #print(afeGridState)
            print(preGridState == afeGridState)
            print("==============between move========================")

            if reward > maxReward:
                best_move = (mid,fid,tgrab)
                maxReward = reward

        self.counter = self.counter + 1
        return best_move
    