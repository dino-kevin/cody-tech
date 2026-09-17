using System;

public class Program
{
  public static void Main(string[] args)
  {
    double number = double.Parse(Console.ReadLine());
    printNumbersDividedBy(number);
  }

  public static void printNumbersDividedBy(double number)
  {
    while (number >= 3.5)
    {
      number = number / 2;
    }

    Console.WriteLine($"{number}");

  }
}
