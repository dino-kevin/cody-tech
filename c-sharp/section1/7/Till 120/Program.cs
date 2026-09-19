using System;

public class Program
{
    public static void Main(string[] args)
    {
        //get user age by parsing the string age from the console readline
        int userAge = int.Parse(Console.ReadLine());
        string finalAge = $"{until_120(userAge)} years till 120";
        Console.WriteLine(finalAge);


    }
    public static int until_120(int userAge)
    {
        int ageAgainst = 120 - userAge;
        return ageAgainst;
    }
}