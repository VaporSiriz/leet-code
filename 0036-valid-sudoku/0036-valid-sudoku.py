class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. row
        for i in range(0, 9):
            number_list = [ field for field in board[i] if field != "." ]
            # print(row)
            if len(number_list) != len(set(number_list)):
                return False
        
        # 2. column
        for i in range(0, 9):
            column = [ board[j][i] for j in range(0, 9) ]
            number_list = [ field for field in column if field != "." ]
            # print(column)
            if len(number_list) != len(set(number_list)):
                return False
            
        # 3. 3x3 sub-boxes
        for i in [0,3,6]:
            for j in [0,3,6]:
                sub_box = sum([
                    [ board[i+x][j+y] for y in range(0,3) ]
                    for x in range(0,3)
                ], [])
                # print(sub_box)
                number_list = [ field for field in sub_box if field != "." ]
                if len(number_list) != len(set(number_list)):
                   return False
    
        return True
    """ i: 0, 3, 6, j:0, 3, 6
         (i,j)   (i,j+1)   (i,j+2)
        (i+1,j) (i+1,j+1) (i+1,j+2)
        (i+2,j) (i+2,j+1) (j+2,j+2)
    """
        
        