using Gtk;
using System;
 
class Hello {
 
        static void Main()
        {
                Application.Init ();
 
                Window window = new Window ("Hello MTE");
                window.Show();
 
                Application.Run ();
 
        }
}
