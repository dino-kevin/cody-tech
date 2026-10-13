using System;   

public class GetElement
{
    public static int getElement(int[][] array, int row, int col)
    {
        if ((row < 0) || (col < 0))
        {
            return -1;
        }
        else
        {
            try
            {
                return array[row][col];

            }

            catch (IndexOutOfRangeException)
            {
                return -1;
            }
        }
    }
}