class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        out = []
        init_x, final_x = 0, len(matrix[0]) - 1
        init_y, final_y = 0, len(matrix) - 1

        while init_x <= final_x and init_y <= final_y:
            for i in range(init_x, final_x + 1):
                out.append(matrix[init_y][i])
            init_y += 1

            for i in range(init_y, final_y + 1):
                out.append(matrix[i][final_x])
            final_x -= 1

            if final_y >= init_y:
                for i in range(final_x, init_x - 1, -1):
                    out.append(matrix[final_y][i])
                final_y -= 1
            
            if final_x >= init_x:
                for i in range(final_y, init_y - 1, -1):
                    out.append(matrix[i][init_x])
                init_x += 1
        return out