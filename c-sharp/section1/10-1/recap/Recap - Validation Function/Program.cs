using System;
using System.Runtime.Serialization;

public class Program
{
    public static bool is_valid(string username, string password)
    {
        // returns the validation bolean of the user and password
        if (username == "admin")
        {
            return password == "pass" || password == "qweasd" ? true : false;
        }

        else if (username == "user")
        {
            return password == "qweasd" ? true : false;
        }

        else
        {
            return false;
        }

    }

    public static void Main(string[] args)
    {
        string user = Console.ReadLine();
        string pass = Console.ReadLine();
        bool res = is_valid(user, pass);
        Console.WriteLine(res);
    }
}