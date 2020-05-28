# This file will be used in the competition
# Please make sure the following functions are well defined

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
        best_move = random.choice(moves)
        for mid,fid,tgrab in moves:
            #move = (mid,fid,tgrab)
            rowIsFull = False
            # Reset the player_state and grid_state to original one before any move
            copyPS = copy.deepcopy(player_state)
            copyGridState = copyPS.grid_state
            #print (copyPS.grid_state)
            #print(copyGridState)
            #print("===========================")
            reward = 0
            tile = tgrab.tile_type #拿出花色
            dest = tgrab.pattern_line_dest #拿出目的地(在右邊的第幾排)
            n2floor = tgrab.num_to_floor_line #要丟掉幾個
            n2pattren = tgrab.num_to_pattern_line #可以放幾個
            reward = (-0.5)*(tgrab.num_to_floor_line) + 0.5*(tgrab.num_to_pattern_line)
            
            if (dest+1) <= n2pattren: #this row is full
                rowIsFull = True
                reward = reward + 1
            #print(reward)
                   
            #copyPS.ExecuteMove(self.id, best_move) #Error

            #update the grid state after this move
            for i in range(5):
                for tile in Tile:
                    if rowIsFull: #The pattern of this row is full
                        grid_color = int(myGridScheme[i][int(tile)])
                        #print(self.grid_color)
                        if int(tile) == grid_color:
                            copyGridState[i][int(tile)] = 1
                            print(copyGridState)
            reward = reward + (copyPS.GetCompletedRows()) * 2 + (copyPS.GetCompletedColumns()) * 7 + (copyPS.GetCompletedSets()) *10
            
            print(reward)
            if reward > maxReward:
                best_move = (mid,fid,tgrab)    
                maxReward = reward
        ##print(myGridScheme)
        ##for tile in Tile:
        ##    print(int(tile)) #turn into numerical BLUE = 0    YELLOW = 1    RED = 2    BLACK = 3    WHITE = 4
        '''
        [[0. 1. 2. 3. 4.]
        [1. 2. 3. 4. 0.]
        [2. 3. 4. 0. 1.]
        [3. 4. 0. 1. 2.]
        [4. 0. 1. 2. 3.]]
        '''

        '''
        for y in range(5):
            for x in range(5):
               print(myGrid[y][x])
        '''
        
        
        
        
            


        
        #print(myGrid[2][1]) can't
        #print(myGrip[3][2]) can't
        #avaMove = player_state.GetAvailableMoves
        #print(game_state.cetre_pool) can't
        
        #after done the move
        '''
        if self.counter > 0:    
            preScore = player_state.ScoreRound[0]
            print(preScore)
        '''

        #print(self.counter)
        
        #print(self.player_trace.moves)
        
        self.counter = self.counter + 1
        return best_move
    