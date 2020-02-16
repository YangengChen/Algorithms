package LeetCode.Java;

import java.util.*;

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int[][] visited = new int[grid.length][grid[0].length];
        int ans = 0;
        for(int row = 0; row < grid.length; row++) {
            for(int col = 0; col < grid[0].length; col++) {
                ans = Math.max(ans, findMaxArea(grid, visited, row, col));
            }
        }
        return ans;
    }
    
    public int findMaxArea(int[][] grid, int[][] visited, int row, int col) {
        if(row == grid.length || col == grid[0].length || 
           row == -1          || col == -1             ||
           visited[row][col] == 1 || grid[row][col] == 0)
            return 0;
        visited[row][col] = 1;
        return 1 + findMaxArea(grid, visited, row-1, col) +
                   findMaxArea(grid, visited, row+1, col) +
                   findMaxArea(grid, visited, row, col-1) +
                   findMaxArea(grid, visited, row, col+1);
    }
}