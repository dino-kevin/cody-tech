using System;

class Program
{
  public static void Main(string[] args)
  {
    printCody(3, 27);
  }

  public static void printCody(int start, int end)
  {
    for (int i = start; i <= end; i++)
    {
      Console.WriteLine($"Hello Coddy: {i}");
    }
  }
}
