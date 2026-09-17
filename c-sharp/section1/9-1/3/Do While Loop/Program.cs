using System;

public class Program {
    public static void Main(string[] args) {
        // Initialize variables
        int sum = 0;
        int number = 1;

        sum = IncrementNumberBy(sum, number);
        // Print the final sum
        Console.WriteLine("Final Sum: " + sum);
    }

    public static int IncrementNumberBy(int sum, int number)
    {
        do
        {
            // Add number to sum
            sum+= number;

            // Increment number by 2 in each iteration
            number+= 2;

            Console.WriteLine($"Sum is: {sum}");
            Console.WriteLine($"Num is: {number}");
        } while(number <= 50);
        return sum;
    }
}
