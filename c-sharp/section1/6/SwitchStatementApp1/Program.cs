using System;

public class Program
{
    public static void Main(string[] args)
    {
        int month = int.Parse(Console.ReadLine());

        string season = GetWeather(month);

        Console.WriteLine(season);
    }

    public static string GetWeather(int month)
    {
        string season = "";

        switch (month)
        {
            case 11:
            case 10:
            case 9:
                season = "Autumn";
                break;
            case 8:
            case 7:
            case 6:
                season = "Summer";
                break;
            case 5:
            case 4:
            case 3:
                season = "Spring";
                break;

            case 2:
            case 1:
            case 12:
                season = "Winter";
                break;

            default:
                season = "none";
                break;
        }
        return season;

    }
}
