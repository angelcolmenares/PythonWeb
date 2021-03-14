using Python.Runtime;
using System;
using System.Collections.Generic;

namespace PythonNet
{    
    public class ModelOne
    {
        private dynamic np;
        private dynamic load_models;
        private dynamic model;
        public ModelOne(string model_path)
        {
            PythonInstance.Execute( ()=>
            {
                dynamic os = Py.Import("os");
                os.environ["TF_CPP_MIN_LOG_LEVEL"] = new PyAnsiString("3");
                os.environ["CUDA_VISIBLE_DEVICES"] = new PyAnsiString( "-1");

                np = Py.Import("numpy");
                dynamic  keras_models = Py.Import("keras.models");
                load_models = keras_models.load_model;
                model = load_models(model_path);
            });
        }

        public double Predict(double v1, double v2, double v3, double v4, double v5, double v6, double v7, double v8)
        {
            var result = PythonInstance.Execute( ()=>
            {
                var input = new List<double>(new double[] { v1, v2,v3,v4,v5,v6,v7,v8});
                dynamic np_input = np.array(input);
                return model.predict(np_input.reshape(1,8));

            });
            return result[0][0];
        }
    }
}