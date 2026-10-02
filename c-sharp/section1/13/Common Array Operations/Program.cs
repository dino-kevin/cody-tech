using System;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;

public class Program
{
    public static double[] CalculateStats(int[] arr)
    {
        int[] numbers = arr;
        int sum = 0;
        foreach (int number in numbers)
        {
            // calculates sum
            sum += number;
        }

        double[] operations = arr.Select(x => (double)x).ToArray();

        // declare of operations of min/max
        int max = numbers[0];
        int min = numbers[0];

        // loop to calculate the min and max
        for (int i = 1; i < numbers.Length; i++)
        {
            if (numbers[i] > max)
            {
                max = numbers[i];
            }
            if (numbers[i] < min)
            {
                min = numbers[i];
            }
        }

        // Sum
        operations[0] = (double)sum;
        // Average
        operations[1] = (double)sum / arr.Length;
        // Min
        operations[2] = max;
        // Max
        operations[3] = min;

        return operations;
    }

    public static void Main(string[] args)
    {
        string text = Console.ReadLine();
        string[] arrString = text.Split(",");
        int[] numbers = new int[arrString.Length];
        for (int i = 0; i < arrString.Length; i++)
        {
            numbers[i] = int.Parse(arrString[i]);
        }
        double[] stats = CalculateStats(numbers);
        Console.WriteLine("Sum: " + stats[0]);
        Console.WriteLine("Average: " + stats[1]);
        Console.WriteLine("Maximum: " + stats[2]);
        Console.WriteLine("Minimum: " + stats[3]);
    }
}