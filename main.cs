using System;

class MainClass {
  public static void Main (string[] args) {
    shutdown = "on"
    Console.WriteLine("////////////////////////////////////");
    Console.WriteLine("////           ///////// //////// //");
    Console.WriteLine("//// ////////////////// //////// ///");
    Console.WriteLine("//// ////////////////            ///");
    Console.WriteLine("//// //////////////// //////// /////");
    Console.WriteLine("//// /////////////// //////// //////");
    Console.WriteLine("//// ////////////// //////// ///////");
    Console.WriteLine("//// ////////////            ///////");
    Console.WriteLine("//// //////////// //////// /////////");
    Console.WriteLine("////           / //////// //////////");
    Console.WriteLine("////////////////////////////////////");
    Console.WriteLine ("Welcome to C# OS!");
    while(shutdown == "on"){
      string input;
      input = Console.ReadLine();
      if (input == "hello")
     { Console.WriteLine("Hello User! Thanks for using this operating system!");
     }
     if (input == "about")
     { Console.WriteLine("Apage C# OS v. 1.0 ");
     }
     if (input == "help")
     { Console.WriteLine("hello = A warm welcome ");
       Console.WriteLine("about = OS version");
     }
     if (input == "shutdown")
     { shutdown == "off"
     }
    }
  }
}

