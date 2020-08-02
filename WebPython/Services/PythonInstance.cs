using Python.Runtime;
using System.IO;

namespace WebPython.Services
{

    public class PythonInstance
    {
        private readonly dynamic python_functions;
        public PythonInstance()
        {
            PythonEngine.Initialize();
            PythonEngine.BeginAllowThreads();
            using (Py.GIL())
            {
                dynamic sys = Py.Import("sys");

                var pyfilesDir = Path.Combine(Directory.GetCurrentDirectory(), "pyfiles");
                sys.path.append(pyfilesDir);

                python_functions = Py.Import("python_functions");
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
