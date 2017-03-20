from copy import deepcopy
class chess(object):
    def __init__(self):
        self.C = True
        self.p = None
#         self.board = self.board()
        self.pos_dict = {'r1':'a1','h1':'b1','b1':'c1','q':'d1','k':'e1','b2':'f1','h2':'g1','r2':'h1',
                        'p1':'a2','p2':'b2','p3':'c2','p4':'d2','p5':'e2','p6':'f2','p7':'g2','p8':'h2',
                        'P1':'a7','P2':'b7','P3':'c7','P4':'d7','P5':'e7','P6':'f7','P7':'g7','P8':'h7',
                         'R1':'a8','H1':'b8','B1':'c8','Q':'d8','K':'e8','B2':'f8','H2':'g8','R2':'h8'}
#     def board(self):
        x = ['a','b','c','d','e','f','g','h']
        y = ['1','2','3','4','5','6','7','8']
        W_Pawn = ['P1','P2','P3','P4','P5','P6','P7','P8']
        W_peceis = ['R','H','B','Q','K','B','H','R']
        B_Pawn = ['p1','p2','p3','p4','p5','p6','p7','p8']
        B_peceis =  ['r','h','b','q','k','b','h','r']
        self.df = pd.DataFrame('-', index=[1,2,3,4,5,6,7,8], columns=['a','b','c','d','e','f','g','h'])
        self.df.loc[1] = B_peceis
        self.df.loc[2] = B_Pawn
        self.df.loc[7] = W_Pawn
        self.df.loc[8] = W_peceis
#         return df
    
    def show_board(self):
        return(self.df)
    
    def move(self,input_str):
        move_pe = input_str[0:2]
        start_pos = input_str[2:4]
        des_pos = input_str[4:6]
        if self.find_key(des_pos) != '-':
            self.pos_dict[self.find_key(des_pos)] = 0
        self.pos_dict[move_pe] = des_pos
        
        self.df[start_pos[0]][int(start_pos[1])] = '-'
        self.df[des_pos[0]][int(des_pos[1])] = move_pe
        
        return(self.df)
    
    def update_pos(self,input_str):
        move_pe = input_str[0:2]
        start_pos = input_str[2:4]
        des_pos = input_str[4:6]
        if self.find_key(des_pos) != '-':
            self.pos_dict[self.find_key(des_pos)] = 0
        self.pos_dict[move_pe] = des_pos
        return(self.pos_dict)
        
           
        
    def find_key(self,value):
        keys = self.pos_dict.keys()
        for i in keys:
            if self.pos_dict[i] == value:
                return(i)
            
        
    
    def game_WL(self):
        pos = deepcopy(self.pos_dict)
        if pos['k'] =='-':
            stop('While Win')
        elif pos['K'] == '-':
            stop('Black win')
        else:
            return(True)
        
        
        
    
#     def move(self,p,start,des):
#         if self.board