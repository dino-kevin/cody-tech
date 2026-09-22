using System;

class Program {
    public static void Main(String[] args) {
      string input = Console.ReadLine();
      string input2 = Console.ReadLine();
      Console.WriteLine(SplitJoinStrings(input, input2));
        
    }
    public static string SplitJoinStrings(string input, string input2)
    {
        string[] result = input.Split(' ');
        return string.Join(input2, result);
    }
}