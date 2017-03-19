import pandas as pd
class chess():
	def __int__(self):
		self.C = True



	def board(self):
		x = ['a','b','c','d','e','f','g','h']
		y = ['1','2','3','4','5','6','7','8']
		W_Pawn = ['P']
		W_peceis = ['R','H','B','Q','K','B','H','R']
		B_Pawn = ['p']
		B_peceis =  ['r','h','b','q','k','b','h','r']
		df = pd.DataFrame('-', index=[1,2,3,4,5,6,7,8], columns=['a','b','c','d','e','f','g','h'])
		df.loc[1] = B_peceis
		df.loc[2] = B_Pawn
		df.loc[7] = W_Pawn
		df.loc[8] = W_peceis
		return df

