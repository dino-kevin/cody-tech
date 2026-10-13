// Write your code only inside the class. Do not write Main() or any code outside this class.
using System;

class PrintMatrix
{
    public static void printMatrix(int[][] matrix)
    {
        if (matrix == null || matrix.Length == 0)
        {
            return;
        }

        for (int i = 0; i < matrix.Length; i++)
        {
            for (int j = 0; j < matrix[i].Length; j++)
            {
                Console.Write(matrix[i][j] + " ");
            }
            Console.WriteLine();
        }
    }
}