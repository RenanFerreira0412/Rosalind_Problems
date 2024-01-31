import 'dart:io';

class DNASolution {
  String currentDir = Directory.current.path;

  late String dna;
  Map<String, int> dnaBases = {'A': 0, 'C': 0, 'G': 0, 'T': 0};

  DNASolution() {
    initialize_dna_sequence();
  }

  // 'pegando' a sequência
  Future<void> initialize_dna_sequence() async {
    try {
      dna = await get_dna_sequence();
      count_dna_bases();
    } catch (e) {
      print("Erro na leitura do arquivo! $e");
    }
  }

  // sequência de DNA
  Future<String> get_dna_sequence() async {
    // caminho do arquivo
    String path = "$currentDir/stronghold/input/rosalind_dna.txt";
    // arquivo
    File inputData = File(path);

    String dnaSequence = await inputData.readAsString();
    return dnaSequence.trim();
  }

  // contando a quantidade de cada base da sequência
  void count_dna_bases() {
    for (var i = 0; i < dna.length; i++) {
      // base
      String base = dna[i];

      // realizando a contagem
      dnaBases.update(base, (value) => value + 1);
    }

    number_dna_bases();
  }

  // número de cada base
  void number_dna_bases() async {
    var numbers = await dnaBases.values;

    try {
      // caminho do arquivo
      String path = "$currentDir/stronghold/output/DNA.txt";
      // arquivo
      File outputData = File(path);
      var f = outputData.openWrite();
      f.write(numbers.join(' '));
      await f.close();
    } catch (e) {
      print("Erro na escrita do arquivo! $e");
    }
  }
}

void main() {
  DNASolution();
}
