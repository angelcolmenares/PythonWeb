using Python.Runtime;
using System.IO;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;

namespace WebPython.Services
{

    public class PythonInstance
    {
        private readonly dynamic python_functions;
        private readonly IConfiguration _configuration;
        private dynamic __models;
        public PythonInstance(IConfiguration configuration)
        {
            _configuration = configuration;
            PythonEngine.Initialize();
            PythonEngine.BeginAllowThreads();
            using (Py.GIL())
            {
                dynamic sys = Py.Import("sys");

                var pyfilesDir = Path.Combine(Directory.GetCurrentDirectory(), "pyfiles");
                sys.path.append(pyfilesDir);

                python_functions = Py.Import("python_functions");

                var model_path= _configuration.GetValue<string>("model_path");
                __models = python_functions.create_model(model_path);


            }
        }

        public double CalculateArea(double widht, double height)
        {
            using (Py.GIL())
            {
                return python_functions.calculate_area(widht, height);
            }
        }

        public AreaResultWithComment CalculateAreaAndComment(double widht, double height)
        {
            using (Py.GIL())
            {
                var pythonResult = python_functions.calculate_area_and_comment(widht, height);
                return new AreaResultWithComment(pythonResult);
            }
        }
        

        public object Predict(double fist, double second){
            using (Py.GIL())
            {
                var input = new List<int>( new int[] { 1,2,3,4,5,6,7,8});                     
                var result = __models.predict( input);
                System.Console.WriteLine(result[0][0]);
                return result;
                
            }
        }
    }

    public class AreaResultWithComment
    {
        public AreaResultWithComment(dynamic pythonResult)
        {
            Value = pythonResult["value"];
            Comment = pythonResult["comment"];
        }

        public double Value { get; private set; }
        public string Comment { get; }
    }

}
