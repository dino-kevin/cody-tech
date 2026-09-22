using System;

public class Program
{
    public static void AnalyzeString(string str)
    {

        Console.WriteLine($"Length: {str.Length}");
        Console.WriteLine($"Substring: {str.Substring(7)}");
        Console.WriteLine($"Substring 2: {str.Substring(0, 5)}");
        Console.WriteLine($"Starts with 'Hello': {str.StartsWith("hello")}");
        Console.WriteLine($"Lowercase: {str.ToLower()}");

    }

    public static void Main(string[] args)
    {
        string message = Console.ReadLine();
        AnalyzeString(message);
    }
}