using System;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Calculator App");
        (double? num1, double? num2) = GetNumbers();
        //PrintNumbers(num1, num2);
        
        // Sum of numbers
        Console.WriteLine($"Sum: {SumNumbers(num1, num2):F2}");

        // Difference of numbers:
        Console.WriteLine($"Difference: {DifferenceNumbers(num1, num2):F2}");

        // Product of numbers:
        Console.WriteLine($"Product: {ProductNumbers(num1, num2):F2}");
        
        // Qoutient of numbers:
        Console.WriteLine($"Quotient: {QuotientNumbers(num1, num2):F2}");

    }

    public static (double? num1, double? num2) GetNumbers()
    {
        string input1 = Console.ReadLine();
        string input2 = Console.ReadLine();

        double d1, d2;

        if (!double.TryParse(input1, out d1) || !double.TryParse(input2, out d2))
            return (null, null);

        return (d1, d2);
    }

    public static double? SumNumbers(double? num1, double? num2)
    {
        double? sum = num1 + num2;
        return sum;
    }

    public static double? DifferenceNumbers(double? num1, double? num2)
    {
        double? difference = num1 - num2;
        return difference;
    }

    public static double? ProductNumbers(double? num1, double? num2)
    {
        double? product = num1 * num2;
        return product;
    }

    public static double? QuotientNumbers(double? num1, double? num2)
    {
        double? quotient = num1 / num2;
        return quotient;
    } 

    public static void PrintNumbers(double? num1, double? num2)
    {
        Console.WriteLine(num1);
        Console.WriteLine(num2);
    }
}
