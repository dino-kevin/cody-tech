using System;
using System.Linq;

public class Program
{
    public static string[] Merge(string[] arr1, string[] arr2)
    {
        return arr1.Concat(arr2).ToArray();
    }

    public static void Main(string[] args)
    {
        string textArr1 = Console.ReadLine();
        string textArr2 = Console.ReadLine();
        string[] arr1 = textArr1.Split(",");
        string[] arr2 = textArr2.Split(",");

        string[] mergedArray = Merge(arr1, arr2);
        Array.Sort(mergedArray, StringComparer.Ordinal);

        Console.WriteLine(string.Join(", ", mergedArray));
    }
}   