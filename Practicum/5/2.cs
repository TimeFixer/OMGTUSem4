using Python.Runtime;
using System;

class Program
{
    static void Main(string[] args)
    {
        using (Py.GIL()) // Инициализация Python
        {
            dynamic sys = Py.Import("sys");
            sys.path.append(@"C:\Users\user\Desktop\OMGTU\Practicum\5"); // Путь к директории

            dynamic script = Py.Import("1"); // Имя файла без .py

            script.main("dataset_10.csv", "new_data.csv");

            dynamic json = Py.Import("json");
            dynamic result = json.load(open("predictions.json"));
            // Вывод предсказаний для каждой модели
            foreach (var model in result.Keys)
            {
                Console.WriteLine($"Predictions for {model}: {result[model]}");
            }
        }
    }
}