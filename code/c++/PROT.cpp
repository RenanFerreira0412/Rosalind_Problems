#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <algorithm>
#include <vector>

class PROTSolution
{
private:
    // não codificam para nenhum aminoácido
    std::string strand_mRNA, protein;
    std::vector<std::string> stop_codons = {"UAA", "UAG", "UGA"};
    std::vector<std::string>::iterator it;

    // codificam para algum aminoácido
    std::map<std::string, char> rna_codon_table = {
        {"UUU", 'F'}, {"CUU", 'L'}, {"AUU", 'I'}, {"GUU", 'V'}, 
        {"UUC", 'F'}, {"CUC", 'L'}, {"AUC", 'I'}, {"GUC", 'V'}, 
        {"UUA", 'L'}, {"CUA", 'L'}, {"AUA", 'I'}, {"GUA", 'V'}, 
        {"UUG", 'L'}, {"CUG", 'L'}, {"AUG", 'M'}, {"GUG", 'V'}, 
        {"UCU", 'S'}, {"CCU", 'P'}, {"ACU", 'T'}, {"GCU", 'A'}, 
        {"UCC", 'S'}, {"CCC", 'P'}, {"ACC", 'T'}, {"GCC", 'A'}, 
        {"UCA", 'S'}, {"CCA", 'P'}, {"ACA", 'T'}, {"GCA", 'A'}, 
        {"UCG", 'S'}, {"CCG", 'P'}, {"ACG", 'T'}, {"GCG", 'A'}, 
        {"UAU", 'Y'}, {"CAU", 'H'}, {"AAU", 'N'}, {"GAU", 'D'}, 
        {"UAC", 'Y'}, {"CAC", 'H'}, {"AAC", 'N'}, {"GAC", 'D'}, 
        {"CAA", 'Q'}, {"AAA", 'K'}, {"GAA", 'E'}, {"CAG", 'Q'}, 
        {"AAG", 'K'}, {"GAG", 'E'}, {"UGU", 'C'}, {"CGU", 'R'}, 
        {"AGU", 'S'}, {"GGU", 'G'}, {"UGC", 'C'}, {"CGC", 'R'}, 
        {"AGC", 'S'}, {"GGC", 'G'}, {"CGA", 'R'}, {"AGA", 'R'}, 
        {"GGA", 'G'}, {"UGG", 'W'}, {"CGG", 'R'}, {"AGG", 'R'}, 
        {"GGG", 'G'}};
        
public:
    PROTSolution(){
        read_strand_mRNA();
        translate_rna_into_protein();
    };

    void read_strand_mRNA() {
        std::ifstream input_data("C:/Programming/Rosalind/input/rosalind_prot.txt");

        if (input_data.is_open()) {
            // lendo a fita de mRNA
            std::getline(input_data, strand_mRNA, '\n');
            
            input_data.close();
        } else {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }

    // traduzir sequência de dna em proteína
    void translate_rna_into_protein() 
    {
        for (unsigned i = 0; i < strand_mRNA.length(); i += 3) 
        {
            // códon da sequência
            std::string codon = strand_mRNA.substr(i, 3);

            // verificando se o códon da sequência não codifica para algum aminoácido
            it = std::find(stop_codons.begin(), stop_codons.end(), codon);

            // códon codifica para algum aminoácido
            if (it == stop_codons.end()) 
            {
                protein += rna_codon_table[codon];
            }
        }
    }

    void get_protein()
    {
        std::ofstream output_data("C:/Programming/Rosalind/output/PROT.txt");

        if (output_data.is_open()) {
            // proteína
            output_data << protein;
            
            output_data.close();
        } else {
            std::cerr << "Não foi possível abrir o arquivo. " << std::endl;
        }
    }
};

int main()
{
    PROTSolution solution;
    solution.get_protein();

    return 0;
}