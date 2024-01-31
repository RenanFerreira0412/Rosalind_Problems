import 'dart:io';

class RNASolution {
  String currentDir = Directory.current.path;

  late String dna;
  late String rna = "";

  RNASolution() {
    initialize_dna_sequence();
  }

  // 'pegando' a sequência
  Future<void> initialize_dna_sequence() async {
    try {
      dna = await get_dna_sequence();
      transcribe();
    } catch (e) {
      print("Erro na leitura do arquivo! $e");
    }
  }

  // sequência de DNA
  Future<String> get_dna_sequence() async {
    // caminho do arquivo
    String path = "$currentDir/stronghold/input/rosalind_rna.txt";
    // arquivo
    File inputData = File(path);

    String rnaSequence = await inputData.readAsString();
    return rnaSequence.trim();
  }

  // contando a quantidade de cada base da sequência
  void transcribe() {
    for (var i = 0; i < dna.length; i++) {
      // base
      String base = dna[i];

      if (base == 'T') {
        rna += 'U';
        continue;
      }

      rna += base;
    }

    get_rna();
  }

  // número de cada base
  void get_rna() async {
    try {
      // caminho do arquivo
      String path = "$currentDir/stronghold/output/RNA.txt";
      // arquivo
      File outputData = File(path);
      var f = outputData.openWrite();
      f.write(rna);
      await f.close();
    } catch (e) {
      print("Erro na escrita do arquivo! $e");
    }
  }
}

void main() {
  RNASolution();
}
