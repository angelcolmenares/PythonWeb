
using Python.Runtime;

namespace PythonNet
{
    public static class NumPy
    {
        public readonly static dynamic np;
        static NumPy()
        {
            np = PythonInstance.Execute(()=> Py.Import("numpy"));
        }

    }
}