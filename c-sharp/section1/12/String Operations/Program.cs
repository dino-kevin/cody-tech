using System;

public class Program {
    public static string CreateFormattedString(string productName, double quantity, double unitPrice) {
        string upperCase = productName.Substring(0, 1).ToUpper();
        string result = productName.Substring(1);
        result = String.Concat(upperCase, result);


        return $"Product: {result}, Quantity: {quantity:F1}, Unit Price: {unitPrice:F5}";
    }

    public static void Main(string[] args) {
        string product = Console.ReadLine();
        double qty = double.Parse(Console.ReadLine());
        double price = double.Parse(Console.ReadLine());
        string formattedString = CreateFormattedString(product, qty, price);
        Console.WriteLine(formattedString);
    }
}