using System;
using System.Diagnostics.CodeAnalysis;

public class Program
{
    public static double CalculateAverageGrade(int[] grades)
    {   
        int sum = 0;;
        foreach (int grade in grades)
        {
            sum+= grade;
        }
        return (double) sum / grades.Length;
    }

    public static void Main(string[] args)
    {
        string text = Console.ReadLine();
        string[] stringArr = text.Split(",");
        int[] studentGrades = new int[stringArr.Length];
        for (int i = 0; i < stringArr.Length; i++)
        {
            studentGrades[i] = int.Parse(stringArr[i]);
        }
        double averageGrade = CalculateAverageGrade(studentGrades);
        Console.WriteLine($"Average grade: {averageGrade}");
    }
}