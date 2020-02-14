package LeetCode.Java;

import java.util.*;


class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> set = new HashSet<>();
        for(int r = 0; r < board.length; r++) {
            for(int c = 0; c < board[0].length; c++) {
                if(board[r][c] == '.') continue;
                int b = (r / 3) * 3 + (c / 3); 
                String row = "r" + r + ':' + board[r][c];
                String col = "c" + c + ':' + board[r][c];
                String blk = "b" + b + ':' + board[r][c];
                if(!set.add(row) || !set.add(col) || !set.add(blk))
                    return false;
            }
        }
        return true;
    }
}