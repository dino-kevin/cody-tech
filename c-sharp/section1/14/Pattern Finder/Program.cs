using System;
using System.Linq;

public class Program
{
    public static void Main(string[] args)
    {
        string arrString1 = Console.ReadLine();
        string arrString2 = Console.ReadLine();

        // Use Trim() to prevent hidden whitespace bugs when inputs have spaces after commas
        string[] str1 = arrString1.Split(',').Select(s => s.Trim()).ToArray();
        string[] str2 = arrString2.Split(',').Select(s => s.Trim()).ToArray();

        Console.WriteLine(isStringPattern(str1, str2));
    }

    public static bool isStringPattern(string[] str1, string[] str2)
    {
        if (str2.Length == 0) return true;
        if (str2.Length > str1.Length) return false;

        // Slide str2 across str1 to find an exact, unbroken match
        for (int i = 0; i <= str1.Length - str2.Length; i++)
        {
            bool match = true;
            for (int j = 0; j < str2.Length; j++)
            {
                if (str1[i + j] != str2[j])
                {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }

        return false;
    }
}