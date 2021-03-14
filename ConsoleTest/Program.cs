using System;
using PythonNet;

namespace ConsoleTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var model_one = new ModelOne("/home/angel/code/WebPython/WebPython/pyfiles/gmm0.9.hdf5");
            var result = model_one.Predict(1,2,3,4,5,6,7,8);
            Console.WriteLine($"result : {result}");
            
        }
    }
}
