﻿using Python.Runtime;
using System.IO;
using System;

namespace PythonNet
{
    public static class PythonInstance
    {
        private static readonly dynamic python_functions;

        static PythonInstance()
        {

            PythonEngine.Initialize();
            PythonEngine.BeginAllowThreads();
            using (Py.GIL())
            {
                dynamic sys = Py.Import("sys");
                var pyfilesDir = Path.Combine(Directory.GetCurrentDirectory(), "pyfiles");
                if (Directory.Exists(pyfilesDir))
                {
                    sys.path.append(pyfilesDir);
                    python_functions = Py.Import("python_functions");
                }

            }
        }

        public static void Execute(Action action)
        {
            using (Py.GIL())
            {
                action();
            }
        }
        public static dynamic Execute(Func<dynamic> action)
        {
            using (Py.GIL())
            {
                return action();
            }
        }
    }
}
