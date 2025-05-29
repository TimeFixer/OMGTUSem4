using System;
using System.IO;
using System.Text.Json; // Для работы с JSON в C#
using Python.Runtime;

namespace PythonCSharpIntegration
{
    class Program
    {
        static void Main(string[] args)
        {
            // Отключение BinaryFormatter
            AppDomain.CurrentDomain.SetData("APP_CONTEXT_DELETE_AUTOMATIC_CLEANUP", true);

            // Путь к python311.dll (замените на ваш путь)
            Runtime.PythonDLL =
                @"C:\Users\user\AppData\Local\Programs\Python\Python311\Python311.dll";
            PythonEngine.Initialize();

            try
            {
                using (Py.GIL())
                {
                    dynamic sys = Py.Import("sys");

                    // Добавляем путь к папке с Python-скриптом
                    string scriptPath = @"C:\Users\user\Desktop\OMGTU\Practicum\5\MyProject";
                    sys.path.append(scriptPath);

                    // Импорт модуля
                    dynamic pyScript = Py.Import("1");

                    // Вызов функции main с тремя аргументами
                    PyObject result = pyScript.main("dataset_10.csv", "new_data.csv");

                    // Вывод результатов
                    Console.WriteLine($"Результаты из питона: {result}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Произошла ошибка:");
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }
            finally
            {
                PythonEngine.Shutdown();
            }
        }
    }
}
