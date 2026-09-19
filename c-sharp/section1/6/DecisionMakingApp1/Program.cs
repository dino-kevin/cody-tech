using System;

public class Program
{
    public static void Main(string[] args)
    {
        int wind = int.Parse(Console.ReadLine()); // Don't change this line
        string status = GetWeatherMessage(wind);

        // Don't change the line below
        Console.WriteLine("status = " + status);
    }

    public static string GetWeatherMessage(int weatherStatus)
    {
        string WeatherMessage = "None";

        if (weatherStatus < 8)
        {
            WeatherMessage = "Calm";
        }

        else if (weatherStatus >= 8 && weatherStatus <= 31)
        {
            WeatherMessage = "Breeze";
        }

        else if (weatherStatus >= 32 && weatherStatus <= 63)
        {
            WeatherMessage = "Gale";
        }

        else
        {
            WeatherMessage = "Storm";
        }

        if (WeatherMessage != "None")
        {
            return WeatherMessage;
        }
        else
        {
            return "None";
        }

    }
}

