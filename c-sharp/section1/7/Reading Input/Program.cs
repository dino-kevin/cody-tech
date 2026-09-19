using System;

public class Program
{
    public static void Main(string[] args)
    {
        // Read the user's name
        string userName = Console.ReadLine();

        // Print the greeting message
        if (userName != "")
        {
            Console.WriteLine($" Hello, {userName}");
        }
    }
}
