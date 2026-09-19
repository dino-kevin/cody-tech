using System;

public class Program {
    public static int productNumbers(int n1, int n2)
    {
        int product = n1 * n2;
        return product;
    }
    
    
    public static void Main(string[] args) 
    {
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());
        // Call the method with a and b as arguments
        Console.WriteLine(productNumbers(a, b));
        
    }
}
