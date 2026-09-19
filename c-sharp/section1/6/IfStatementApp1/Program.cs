using System;

public class Program
{
    public static void Main(string[] args)
    {
        int a = 11;
        int b = 10;

        // Don't change below this line
        int c = 0;
        if (a >= b && !(b < 10))
        {
            c = 2;
        }

        c += 1;
        Console.WriteLine("c = " + c);
    }
}
