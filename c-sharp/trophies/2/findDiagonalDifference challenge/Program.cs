using System;
public class FindDiagonalDifference
{
    public static int findDiagonalDifference(int[][] matrix)
    {
        int primaryDiagonalSum = 0;
        int secondaryDiagonalSum = 0;

        for (int i = 0; i < matrix.Length; i++)
        {
            primaryDiagonalSum += matrix[i][i];
            secondaryDiagonalSum += matrix[i][matrix.Length - i - 1];
        }

        return Math.Abs(primaryDiagonalSum - secondaryDiagonalSum);
    }
}