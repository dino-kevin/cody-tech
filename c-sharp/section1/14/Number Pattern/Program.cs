using System;

public class Program
{
    public static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        createPiramid(n);
    }

    public static void createPiramid(int n)
    {
        for (int i = 1; i < n + 1; i++)
        {
            if (i % 2 == 1)
            {
                string str = new string('*', i);
                Console.WriteLine(str);
            }
        }
    }
}