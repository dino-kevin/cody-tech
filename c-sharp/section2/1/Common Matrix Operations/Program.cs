using System.Diagnostics.CodeAnalysis;

public class MultiplyMatrices
{
    // Implement the MultiplyMatrices method
    public static int[][] multiplyMatrices(int[][] matrix1, int[][] matrix2)
    {   
        int [][] product_matrix = new int [matrix1.Length][];
        
        for (int i = 0; i < matrix1.Length; i++)
        {
            product_matrix[i] = new int[matrix2[0].Length];
            
            for (int j = 0; j < matrix2[0].Length; j++)
            {   
                for (int k = 0; k < matrix1[i].Length; k++)
                {
                    product_matrix[i][j]+= matrix1[i][k] * matrix2[k][j];
                }
                
            }
        }

        return product_matrix;
        
    }
}