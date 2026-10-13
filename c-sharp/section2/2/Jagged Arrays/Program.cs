public class CreateTriangle
{
    public static int[][] createTriangle(int size)
    {
        // 1. Allocate the outer array
        int[][] triangle = new int[size][];

        for (int i = 0; i < size; i++)
        {
            // 2. Allocate each row (size depends on triangle shape, e.g., i + 1)
            triangle[i] = new int[i + 1];

            for (int j = 0; j < triangle[i].Length; j++)
            {
                triangle[i][j] = i + j;
            }
        }

        return triangle;
    }
}