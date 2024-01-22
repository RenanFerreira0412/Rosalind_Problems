#include <iostream>
#include <map>
#include <fstream>
#include <string>

class DNASolution
{
private:
    std::string dna_seq;
    std::map<char, int> dna_bases = {
        {'A', 0}, // Adenina
        {'T', 0}, // Timina
        {'C', 0}, // Citocina
        {'G', 0}  // Guanina
    };

public:
    // Lendo a sequência do DNA
    void read_dna_seq()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_dna.txt");

        if (input_data.is_open())
        {
            // lendo os dados
            std::getline(input_data, dna_seq, '\n');

            input_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    // Contando a qtd. de cada base do DNA
    void count_dna_bases()
    {
        for (auto base : dna_seq)
        {
            dna_bases[base]++;
        }
    }

    // Retornando o número de cada base do DNA
    void number_of_each_dna_bases()
    {
        read_dna_seq();
        count_dna_bases();

        std::ofstream output_data("C:/Programming/Rosalind/output/DNA.txt");

        if (output_data.is_open())
        {
            for (auto base : dna_bases)
            {
                output_data << base.second << " ";
            }
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }
};

int main()
{
    DNASolution solution;
    solution.number_of_each_dna_bases();

    return 0;
}