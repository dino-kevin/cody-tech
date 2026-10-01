using System;

public class Program {
    public static void Main(string[] args) {
        // Initialize the fruits array
        string [] fruits = {"apple", "banana", "orange", "grape","kiwi"};


        // Use a foreach loop to iterate over the array
        foreach (string fruit in fruits)
        {
            Console.WriteLine($"{fruit.ToUpper()}");
        }
    }
}