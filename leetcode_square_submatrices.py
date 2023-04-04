#https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution(object):
    # Returns 1 if all 1s  in the matrix
    def allOnes(self, start_row, start_column, size, matrix):
        max_rows = len(matrix)
        max_columns = len(matrix[0])
        #print('max rows=', max_rows)
        #print('max columsn=', max_columns)
        print('start_row=%d start_col=%d size=%d' % (start_row, start_column, size))
        # return 1
        if start_row+size <= max_rows and start_column+size <= max_columns:
            for row in range(start_row, start_row+size):
                if min(matrix[row][start_column:start_column+size]) == 0:
                    return 0
            return 1
        return 0


    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        max_rows = len(matrix)
        max_columns = len(matrix[0])
        submatrics_with_all_1s = 0
        for row in range(max_rows):
            print(matrix[row])
        for size in range(1,1+min(max_rows, max_columns)):
            print('\n\n\n')
            for start_row in range(max_rows):
                for start_column in range(max_columns):
                    x = self.allOnes(start_row, start_column, size, matrix)
                    submatrics_with_all_1s += x
                    print('submatrics_with_all_1s=', x)
        return(submatrics_with_all_1s)



def main():
    matrix = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]
    matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
matrix = [[0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1],[1,1,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0],[0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0],[0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1],[1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1],[0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1],[1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0],[1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1],[1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,1],[1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],[1,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1],[0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1],[1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1],[1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,0,0],[1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0],[1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1],[1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0],[0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0],[1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1],[0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0],[0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1],[1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,0],[1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1],[0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0],[0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0],[1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1],[0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1],[0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1],[1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0],[0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0],[0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1],[0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0],[1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1],[1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0],[1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0],[1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,0],[0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1],[0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0],[1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1],[0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1],[0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1],[0,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1],[1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1],[0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0],[0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0],[1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0],[0,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,1],[0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,1],[1,1,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1],[1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1],[0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1],[0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0],[1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0],[0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1],[1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0],[1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1],[0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0],[0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1],[1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1],[0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1],[0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1],[0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0],[1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0],[0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0],[1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1],[0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0],[1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0],[1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],[0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0],[1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0],[1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0],[1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1],[0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],[1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1],[1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1],[0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1],[1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,... 44137 more chars
    print(Solution().countSquares(matrix))

if __name__ == "__main__":
    main()