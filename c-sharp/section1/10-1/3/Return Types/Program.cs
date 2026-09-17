using System;

public class Program
{
    public static void Main(string[] args)
    {

        int iterations = int.Parse(Console.ReadLine());
        double num1 = double.Parse(Console.ReadLine());
        double num2 = double.Parse(Console.ReadLine());
        double? result = Bigger(num1, num2);
        DivideNumbers(result, iterations);
    
    }

    public static double? Bigger(double arg1, double arg2)
    {
        double? biggerNumber = (arg1 > arg2) ? arg1 : arg2;

        if (arg1 == arg2)
        {
            Random random = new Random();
            double randomNumber = random.NextDouble() <= arg1 ? arg1 : arg2;
            return randomNumber;
        }

        else
        {
            return biggerNumber;
        }

    }

    public static void DivideNumbers(double? result, int iterations){    

        for (int i = 0; i < iterations; i++)
        {
            if (result <= 2.9)
            {
                break;
            }

            else
            {
                result = result / 2;
                Console.WriteLine($"{result}");
            }

        }
    }
}
