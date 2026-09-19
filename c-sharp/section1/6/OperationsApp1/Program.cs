using System;

public class Program
{
    public static void Main(string[] args)
    {
        int n1 = int.Parse(Console.ReadLine());
        int n2 = int.Parse(Console.ReadLine());
        string op = Console.ReadLine();

        double result = CalculateResult(n1, n2, op);
        Console.WriteLine(result);
    }

    public static double CalculateResult(int n1, int n2, string op)
    {
        switch (op)
        {
            case "+":
                return n1 + n2;
                break;
            case "-":
                return n1 - n2;
                break;
            case "/":
                return n1 / n2;
                break;
            case "*":
                return n1 * n2;
                break;
            default:
                return 0;
                break;
        }
    }
}
