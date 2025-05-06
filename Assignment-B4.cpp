#include <iostream>
#include <vector>
using namespace std;

// Function to check if it's safe to place a queen
bool isSafe(vector<vector<int>>& board, int row, int col, int n) {
    // Check column
    for (int i = 0; i < row; i++)
        if (board[i][col] == 1)
            return false;

    // Check upper-left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    // Check upper-right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
        if (board[i][j] == 1)
            return false;

    return true;
}

// Function to print the board
void printBoard(const vector<vector<int>>& board) {
    int n = board.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (board[i][j] ? "Q " : ". ");
        }
        cout << endl;
    }
    cout << "---------------------\n";
}

// Solve and show one solution with steps
bool solveNQueenStepwise(vector<vector<int>>& board, int row, int n) {
    if (row == n) {
        cout << "\n✅ Final Solution Found:\n";
        printBoard(board);
        return true;
    }

    for (int col = 0; col < n; col++) {
        cout << "Trying to place Queen at Row " << row << ", Column " << col << "...\n";
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1;
            printBoard(board);
            if (solveNQueenStepwise(board, row + 1, n))
                return true;
            // Backtrack
            cout << "Backtracking from Row " << row << ", Column " << col << "\n";
            board[row][col] = 0;
            printBoard(board);
        } else {
            cout << "Position Row " << row << ", Column " << col << " is NOT safe.\n";
        }
    }
    return false;
}

// Recursive function to get all solutions
void solveAllNQueens(vector<vector<int>>& board, int row, int n, int& count) {
    if (row == n) {
        count++;
        cout << "Solution #" << count << ":\n";
        printBoard(board);
        return;
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1;
            solveAllNQueens(board, row + 1, n, count);
            board[row][col] = 0; // backtrack
        }
    }
}

// Main function
int main() {
    int n;
    cout << "Enter the number of queens (n): ";
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n, 0));

    cout << "\n🔁 Stepwise Trace to Find One Solution:\n";
    if (!solveNQueenStepwise(board, 0, n))
        cout << "❌ No solution exists for " << n << " queens.\n";

    cout << "\n📋 Listing All Possible Solutions:\n";
    int totalSolutions = 0;
    solveAllNQueens(board, 0, n, totalSolutions);
    cout << "\n✅ Total number of solutions = " << totalSolutions << endl;

    return 0;
}