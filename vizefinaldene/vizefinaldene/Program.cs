using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vizefinaldene
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double vize, final, sonuc;
            Console.WriteLine("Vize:");
            vize = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Final:");
            final = Convert.ToDouble(Console.ReadLine());
            sonuc = (vize * 0.40) + (final * 0.60);
            Console.WriteLine("Ortalamanız:" + Convert.ToString(sonuc));
            if(sonuc < 41)
            {
                Console.WriteLine("Kaldınız..");
            }
            else if(final < 41)
            {
                Console.WriteLine("final notundan Kaldınız!");
            }
            else
            {
                Console.WriteLine("Geçtiniz!");
            }
            Console.WriteLine("Program sonlanıyor..");
            Console.Read();
            

        }
    }
}
