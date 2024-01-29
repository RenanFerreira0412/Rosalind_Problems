#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

class ORFSolution
{
private:
    std::string dna_seq, dna_reverse_comp_seq, start_codon = "ATG";
    // proteínas
    std::vector<std::string> proteins;
    // não codificam para nenhum aminoácido
    std::vector<std::string> stop_codons = {"TAA", "TAG", "TGA"};
    std::map<char, char> complements = {
        {'A', 'T'}, {'T', 'A'}, {'G', 'C'}, {'C', 'G'}};

    // codificam para algum aminoácido
    std::map<std::string, char> rna_codons = {
        {"UUU", 'F'}, {"CUU", 'L'}, {"AUU", 'I'}, {"GUU", 'V'}, {"UUC", 'F'}, {"CUC", 'L'}, 
        {"AUC", 'I'}, {"GUC", 'V'}, {"UUA", 'L'}, {"CUA", 'L'}, {"AUA", 'I'}, {"GUA", 'V'}, 
        {"UUG", 'L'}, {"CUG", 'L'}, {"AUG", 'M'}, {"GUG", 'V'}, {"UCU", 'S'}, {"CCU", 'P'}, {"ACU", 'T'}, {"GCU", 'A'}, {"UCC", 'S'}, {"CCC", 'P'}, {"ACC", 'T'}, {"GCC", 'A'}, {"UCA", 'S'}, {"CCA", 'P'}, {"ACA", 'T'}, {"GCA", 'A'}, {"UCG", 'S'}, {"CCG", 'P'}, {"ACG", 'T'}, {"GCG", 'A'}, {"UAU", 'Y'}, {"CAU", 'H'}, {"AAU", 'N'}, {"GAU", 'D'}, {"UAC", 'Y'}, {"CAC", 'H'}, {"AAC", 'N'}, {"GAC", 'D'}, {"CAA", 'Q'}, {"AAA", 'K'}, {"GAA", 'E'}, {"CAG", 'Q'}, {"AAG", 'K'}, {"GAG", 'E'}, {"UGU", 'C'}, {"CGU", 'R'}, {"AGU", 'S'}, {"GGU", 'G'}, {"UGC", 'C'}, {"CGC", 'R'}, {"AGC", 'S'}, {"GGC", 'G'}, {"CGA", 'R'}, {"AGA", 'R'}, {"GGA", 'G'}, {"UGG", 'W'}, {"CGG", 'R'}, {"AGG", 'R'}, {"GGG", 'G'}};

    std::vector<std::string>::iterator it;

public:
    ORFSolution()
    {
        read_dna_seq();
        open_reading_frame();
    }

    // inverter sequência
    void reverse(std::string &complement)
    {
        int n = complement.length();

        for (int i = 0; i < n / 2; ++i)
        {
            std::swap(complement[i], complement[n - i - 1]);
        }
    }

    // definir complemento
    std::string get_complement(std::string dna)
    {
        std::string dna_comp;

        for (auto base : dna)
        {
            dna_comp += complements[base];
        }

        return dna_comp;
    }

    // transcrever sequência de DNA
    void transcribe_dna(std::string &dna)
    {
        // T(timina) -> U(uracila)
        std::replace(dna.begin(), dna.end(), 'T', 'U');
    }

    // traduzir RNA
    void translate_rna(std::string &rna)
    {
        std::string protein;
        for (unsigned i = 3; i < rna.length(); i += 3)
        {
            // códon da sequência
            std::string codon = rna.substr(i - 3, 3);

            protein += rna_codons[codon];
        }

        if (!protein.empty())
        {
            proteins.push_back(protein);
        }
    }

    // lendo a sequência de DNA
    void read_dna_seq()
    {
        std::ifstream input_data("../../input/rosalind_orf.txt");

        std::string line;

        if (input_data.is_open())
        {
            // lendo as linhas do arquivo
            while (std::getline(input_data, line, '\n'))
            {
                // verificando se não é o rótulo
                if (line[0] != '>')
                {
                    // lendo a sequência do DNA
                    dna_seq += line;
                }
            }
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo!" << std::endl;
        }

        // definindo o complemento
        std::string dna_comp = get_complement(dna_seq);
        // invertendo a sequência
        reverse(dna_comp);
        // atualizando a variável
        dna_reverse_comp_seq = dna_comp;

        std::cout << dna_seq << std::endl;
        std::cout << dna_reverse_comp_seq << std::endl;
    }

    // lendo os frames
    void read_frames(std::string dna, unsigned start)
    {
        std::string rna;
        int init = -1;
        for (unsigned i = start + 3; i < dna.length(); i += 3)
        {
            std::string codon = dna.substr(i - 3, 3);

            // começo da sequência
            if (codon == start_codon)
            {
                init = 1;
            }

            // verificando se o códon da sequência não codifica para algum aminoácido
            it = std::find(stop_codons.begin(), stop_codons.end(), codon);

            // término da sequência
            if (it != stop_codons.end())
            {
                init = 0;
                std::cout << "RNA: " << rna << std::endl;


                // processo de tradução
                translate_rna(rna);
                // limpando a sequência
                rna.clear();
            }

            if (init == 1)
            {
                rna += codon;
            }
        }

        // "TAA", "TAG", "TGA"
        // ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA        ATGATCCGAGTAGCATCT
        // ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA GCCTGA ATGATCCGAGTAGCATCTCAG
    }

    void open_reading_frame()
    {
        // frames
        read_frames(dna_seq, 0);
        read_frames(dna_seq, 1);
        read_frames(dna_seq, 2);

        read_frames(dna_reverse_comp_seq, 0);
        read_frames(dna_reverse_comp_seq, 1);
        read_frames(dna_reverse_comp_seq, 2);
    }

    void get_proteins()
    {
        std::ofstream output_data("../../output/ORF.txt");

        if (output_data.is_open())
        {
            for (auto protein : proteins)
            {
                output_data << protein << '\n';
            }
        }
        else
        {
            std::cerr << "Não foi possível abrir o arquivo!" << std::endl;
        }
    }
};

int main()
{
    ORFSolution solution;
    solution.get_proteins();

    return 0;
}