#include <iostream>
#include <fstream>
#include <map>
#include <string>

class REVCSolution
{
private:
    std::string dna_seq, comple_seq, revc;

public:
    // lendo a sequência de DNA
    void read_dna_seq()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_revc.txt");

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

    // inverter a sequência do complemento de dna
    std::string reverse(std::string sequence)
    {
        std::string newSequence;
        for (int i = sequence.length() - 1; i >= 0; --i)
        {
            newSequence += sequence[i];
        }
        return newSequence;
    }

    // pegar o complemento da sequência de dna
    void set_complement()
    {
        std::map<char, char> complement = {{'A', 'T'}, {'T', 'A'}, {'C', 'G'}, {'G', 'C'}};

        for (auto base : dna_seq)
        {
            comple_seq += complement[base];
        }
    }

    void get_reverse_complement()
    {
        read_dna_seq();
        set_complement();
        revc = reverse(comple_seq);

        std::ofstream output_data("C:/Programming/Rosalind/output/REVC.txt");

        if (output_data.is_open())
        {
            output_data << revc;

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
    REVCSolution solution;
    solution.get_reverse_complement();

    return 0;
}