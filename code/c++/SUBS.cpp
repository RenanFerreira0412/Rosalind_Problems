#include <iostream>
#include <string>
#include <fstream>
#include <vector>

class SUBSSolution
{
private:
    std::string dna_seq_one, dna_seq_two;
    std::vector<unsigned> locations;

public:
    SUBSSolution()
    {
        read_dna_seq();
        check_locations();
    }

    void read_dna_seq()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_subs.txt");
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

    // verificando as localizações da substring
    void check_locations()
    {
        unsigned substr_size = dna_seq_two.length();

        for (unsigned i = 0; i < dna_seq_one.length() - substr_size + 1; ++i)
        {
            if (dna_seq_one.substr(i, substr_size) == dna_seq_two)
            {
                locations.push_back(i + 1);
            }
        }
    }

    void get_locations()
    {
        std::ofstream output_data("C:/Programming/Rosalind/output/SUBS.txt");

        if (output_data.is_open())
        {
            for (auto location : locations)
            {
                output_data << location << " ";
            }
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
    SUBSSolution solution;
    solution.get_locations();

    return 0;
}