using System;

public class Program
{
    public static void Main(string[] args)
    {
        int count = int.Parse(Console.ReadLine());
        int sum = 0;

        // Sum of all numbers
        for (int i = 1; i <= count; i++)
        {
            int number = int.Parse(Console.ReadLine());
            sum += number;
        }
        Console.WriteLine($"{sum}");

    }

}