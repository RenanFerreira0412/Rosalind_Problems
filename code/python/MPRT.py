import requests
import os


class MPRTSolution:
    def __init__(self):
        self.uniprot_ids = []
        self.proteins = []
        self.locations = {}

        self.read_uniprot_ids()
        self.get_proteins()
        self.find_motif()

    # lendo os IDs de acesso para as proteínas no Banco de Dados UniProt
    def read_uniprot_ids(self):
        try:
            path = os.path.realpath("../../input/rosalind_mprt.txt")
            input_data = open(path, 'r')
            # linhas de texto
            ids = input_data.readlines()
            # IDs de acesso
            self.uniprot_ids = [id.strip() for id in ids]
            input_data.close()

        except IOError:
            print("Erro na leitura do arquivo!")

    # acessar as proteínas
    def access_proteins_by(self, uniprot_id: str):
        url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text
                protein = ''.join(data.split('\n')[1:-1])
                self.proteins.append(protein)
        except requests.HTTPError as e:
            print(f"Erro no acesso aos dados: {e}")

    # acessar proteínas
    def get_proteins(self):
        for i in range(len(self.uniprot_ids)):
            id = self.uniprot_ids[i].split('_')[0]
            self.access_proteins_by(id)

    def check_location(self, location: str):
        n = 0

        if location[1] != 'P' and location[3] != 'P':
            n += 2

        if location[0] == 'N':
            n += 1

        if location[2] in ['S', 'T']:
            n += 1

        return n == len(location)

    # encontar o motivo
    def find_motif(self):
        for i in range(len(self.proteins)):
            protein = self.proteins[i]
            starts = []
            j = 0
            while j < len(protein)-4:
                # localizações na proteína
                location = protein[j:j+4]

                # verificando se a região é um motivo (motif)
                is_motif = self.check_location(location)

                if is_motif:
                    # adicionando o começo das localizações
                    starts.append(j+1)
                j += 1

            if len(starts) != 0:
                self.locations[self.uniprot_ids[i]] = starts

    # Protein Motif

    def protein_motif(self):
        try:
            path = os.path.realpath("../../output/MPRT.txt")
            output_data = open(path, 'w')
            for id, starts in self.locations.items():
                output_data.write(f"{id}\n")
                output_data.write(f"{' '.join(map(str, starts))}\n")
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = MPRTSolution()
    solution.protein_motif()
