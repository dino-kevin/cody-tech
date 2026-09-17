using System;

public class Program
{

    public static void Main(string[] args)
    {
        DisplayMessage("Hello!");
        DisplayMessage("Coddy", 3);
    }

    public static void DisplayMessage(string message, int repeatCount = 1)
    {
        for (int i = 1; i <= repeatCount; i++)
        {
            Console.WriteLine($"{message}");
        }
    }
}