#include <iostream>
#include <string>
#include <fstream>

class HAMMSolution
{
private:
    std::string dna_seq_one, dna_seq_two;
    int hamming_distance = 0;

public:
    HAMMSolution()
    {
        read_dna_seq();
    }

    void read_dna_seq()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_hamm.txt");
        std::string line;
        int num_line = 1;

        if (input_data.is_open())
        {
            while (std::getline(input_data, line, '\n'))
            {
                if (num_line == 1)
                {
                    dna_seq_one = line;
                    num_line++;
                    continue;
                }

                dna_seq_two = line;
            }
            input_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    void get_hamming_distance()
    {

        for (unsigned i = 0; i < dna_seq_one.length(); ++i)
        {
            if (dna_seq_one[i] != dna_seq_two[i])
            {
                hamming_distance++;
            }
        }

        std::ofstream output_data("C:/Programming/Rosalind/output/HAMM.txt");

        if (output_data.is_open())
        {
            output_data << hamming_distance;
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
    HAMMSolution solution;
    solution.get_hamming_distance();

    return 0;
}