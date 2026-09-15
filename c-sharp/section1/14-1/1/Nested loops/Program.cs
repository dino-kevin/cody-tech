using System;

public class Program {
    public static void Main(string[] args) {
        int width = int.Parse(Console.ReadLine());
        int height = int.Parse(Console.ReadLine());
        
        Rectangle(width, height);

    }

    public static void Rectangle(int width, int height)
    {
        for (int i = 0; i <height; i++)
        {
            string stars = new string('*', width);
            Console.WriteLine(stars);
        }
    }
}