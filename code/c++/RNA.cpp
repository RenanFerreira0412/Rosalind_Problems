#include <iostream>
#include <string>
#include <fstream>

class RNASolution
{
private:
    std::string dna_seq, rna_seq;

public:
    // lendo a sequência de DNA
    void read_dna_seq()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_rna.txt");

        if (input_data.is_open())
        {
            std::getline(input_data, dna_seq, '\n');

            input_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    // transcrição da sequência de DNA para RNA
    void transcribing_dna_to_rna()
    {
        for (auto base : dna_seq)
        {
            if (base == 'T')
            {
                rna_seq += 'U';
                continue;
            }
            rna_seq += base;
        }
    }

    // escrevendo a sequência de rna
    void get_rna_seq()
    {
        read_dna_seq();
        transcribing_dna_to_rna();

        std::ofstream output_data("C:/Programming/Rosalind/output/RNA.txt");

        if (output_data.is_open())
        {
            output_data << rna_seq;

            output_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }
};

int main()
{
    RNASolution solution;
    solution.get_rna_seq();

    return 0;
}