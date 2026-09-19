using System;

public class Program {
    public static int[] Reverse(int[] arr) {
        int [] reverseNumbers = new int[arr.Length];
        for (int i = 0; i < arr.Length; i++)
        {
            reverseNumbers[arr.Length - i - 1] = arr[i];
        }

        return reverseNumbers;
       
    }

    public static void Main(string[] args) {
        string text = Console.ReadLine();
        string[] stringArr = text.Split(",");
        int[] arr = new int[stringArr.Length];
        for (int i = 0; i < stringArr.Length; i++) {
            arr[i] = int.Parse(stringArr[i]);
        }
        
        int[] result = Reverse(arr);
        Console.WriteLine("The reversed array is: " + string.Join(", ", result));
    }
}
