using System;
using System.Linq;

public class Program
{
    public static int Prod(int[] arr)
    {
        int result = arr.Aggregate(1, (acc, x) => acc * x);
        return result;
    }
    public static void Main(string[] args)
    {
        string text = Console.ReadLine();
        string[] stringArr = text.Split(',');
        int[] arr = new int[stringArr.Length];
        for (int i = 0; i < stringArr.Length; i++)
        {
            arr[i] = int.Parse(stringArr[i]);
        }

        int result = Prod(arr);
        Console.WriteLine("Product of array elements: " + result);
    }
}