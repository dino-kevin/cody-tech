using System;

public class Program
{
    public static void Main(string[] args)
    {
        int number = int.Parse(Console.ReadLine());
        string result = (number > 0) ? "positive" : checkNumber(number);

        Console.WriteLine("The number is " + result);
    }

    public static string checkNumber(int number)
    {
        if (number == 0)
            return "zero";
        else
            return "negative";
    }
}
