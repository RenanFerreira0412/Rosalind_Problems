#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class IPRBSolution
{
private:
    // população total
    int pop;
    // número de homozigotos dominantes, heterozigotos e homozigotos recessivos
    int k, m, n;

public:
    IPRBSolution()
    {
        get_individuals();
    };

    // número de indivíduos
    void get_number_of_individuals(std::string line)
    {
        // indivíduos
        std::vector<int> individuals;
        // quantidade de cada indivíduo
        std::string quantity;

        for (auto c : line)
        {
            if (!isspace(c))
            {
                quantity += c;
                continue;
            }

            std::cout << quantity << std::endl;
            // adicionando a quantidade de indivíduos
            individuals.push_back(std::stoi(quantity));
            quantity = "";
        }
        individuals.push_back(std::stoi(quantity));


        k = individuals[0]; // número de homozigotos dominantes
        m = individuals[1]; // número de heterozigotos
        n = individuals[2]; // número de homozigotos recessivos

        pop = k + m + n; // população
    }

    // pegando os indivíduos
    void get_individuals()
    {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_iprb.txt");
        // linha de texto
        std::string line;

        if (input_data.is_open())
        {
            // lendo a linha de texto
            std::getline(input_data, line, '\n');

            // número de indivíduos
            get_number_of_individuals(line);

            input_data.close();
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    // calcular probabilidade
    int cal_probability()
    {
        int probability;

        probability = (k * (k - 1) + m * (m - 1) * 0.75 + 2 * (k * m + k * n + m * n * 0.5)) / pop * (pop - 1);

        return probability;
    }

    // probabilidade
    void probability()
    {
        std::ofstream output_data("C:/Programming/Rosalind/output/IPRB.txt");

        if (output_data.is_open())
        {
            output_data << cal_probability();
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
    IPRBSolution solution;
    solution.probability();

    return 0;
}