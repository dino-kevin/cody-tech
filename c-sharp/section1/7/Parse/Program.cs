using System;

public class Program
{
    public static void Main(string[] args)
    {
        string firstNumberString = Console.ReadLine();
        string secondNumberString = Console.ReadLine();

        // Use Parse to convert the numbers
        int firstNumber = int.Parse(firstNumberString);
        int secondNumber = int.Parse(secondNumberString);

        // Print the sum of the numbers
        int result = firstNumber + secondNumber;  
        Console.WriteLine(result);
        
    }
}