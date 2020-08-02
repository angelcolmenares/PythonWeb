using Microsoft.AspNetCore.Mvc;
using WebPython.Services;

namespace WebPython.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PythonCalculatorController : ControllerBase
    {
        private readonly PythonInstance _python;

        public PythonCalculatorController(PythonInstance python)
        {
            _python = python;
        }

        [HttpGet("calculate-area")]
        public double CalculateArea([FromQuery] double width, double height)
        {           
            return _python.CalculateArea(width, height);
        }

        [HttpGet("calculate-area-and-comment")]
        public AreaResultWithComment CalculateAreaAndComment([FromQuery] double width, double height)
        {
            return _python.CalculateAreaAndComment(width, height);
        }
    }
}
