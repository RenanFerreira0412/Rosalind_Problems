#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <iomanip>

class GCSolution
{
private:
    std::vector<std::string> labels;
    std::vector<double> gc_content_freq;

public:
    GCSolution()
    {
        read_dna_fasta_format();
    }

    // calcular a frequência GC no DNA
    double count_gc_content_freq(std::string dna)
    {
        double quantity = 0;

        for (auto base : dna)
        {
            if (base == 'G' || base == 'C')
            {
                quantity++;
            }
        }

        double freq = 100 * quantity / dna.length();

        return freq;
    }

    // lendo o DNA no formato FASTA
    void read_dna_fasta_format()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_gc.txt");
        std::string line, dna_seq;
        double frequency;

        if (input_data.is_open())
        {
            // lendo a linha de texto
            while (std::getline(input_data, line, '\n'))
            {

                // verificando se a linha é o rótulo da sequência de DNA
                if (line[0] == '>')
                {
                    // adicionando os rótulo
                    labels.push_back(line.substr(1));

                    // adicionando a sequência de DNA
                    if (!dna_seq.empty())
                    {
                        frequency = count_gc_content_freq(dna_seq);
                        gc_content_freq.push_back(frequency);
                        dna_seq.clear();
                    }

                    continue;
                }

                dna_seq += line;
            }
            // adicionando a última sequência de DNA lida
            frequency = count_gc_content_freq(dna_seq);

            gc_content_freq.push_back(frequency);

            input_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    // verificar o índice da maior frequência
    unsigned check_max(std::vector<double> frequency)
    {
        double high = frequency[0];
        unsigned pos = 0;
        for (unsigned i = 1; i < frequency.size(); ++i)
        {
            if (frequency[i] > high)
            {
                high = frequency[i];
                pos = i;
            }
        }
        return pos;
    }

    void get_highest_gc_content()
    {
        unsigned i = check_max(gc_content_freq);

        std::ofstream output_data("C:/Programming/Rosalind/output/GC.txt");

        if (output_data.is_open())
        {
            output_data << labels[i] << '\n';
            output_data << std::fixed << std::setprecision(6) << gc_content_freq[i] << '\n';
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }
};

int main()
{
    GCSolution solution;
    solution.get_highest_gc_content();

    return 0;
}
