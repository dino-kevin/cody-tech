using System;

public class Program {
    public static void Main(string[] args) {
        int inputUser = int.Parse(Console.ReadLine());
        Console.WriteLine(checkInputUser(inputUser));

    }
    public static string checkInputUser(int inputUser)
    {
        if (inputUser == 1)
        {
            return "T";
        }

        else
        {
            return "F";
        }

    }
}