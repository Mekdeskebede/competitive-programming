class solution:
    def soln(self,array):
    
        def dfs( x_range, y_range):
            for i in range(len(array)):
                if (x_range[0] < (array[i][0] - array[i][2]) < x_range[1] or x_range[0] < (array[i][0] + array[i][2]) < x_range[1]) and (y_range[0] < (array[i][1] - array[i][2]) < y_range[1] or y_range[0] < (array[i][1] + array[i][2]) < y_range[1]):
                    dfs((min(x_range[0],array[i][0] - array[i][2]),max(x_range[1])))

