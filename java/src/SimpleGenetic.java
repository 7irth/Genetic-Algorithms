import java.text.CharacterIterator;
import java.text.StringCharacterIterator;

public class SimpleGenetic {
    public static void main(String[] args) {
        Chromosome test = new Chromosome();
        System.out.println(test);
        test.chromosomeValue();
    }

    private static class Chromosome {

        String genes = "";
        int codonSize = 4;
        int numberOfGenes = 8;
        int length = codonSize * numberOfGenes;
        int maxValue = (int) Math.pow(9, (numberOfGenes / 2) + 1);
        int value = maxValue;

        public Chromosome() {
            while (genes.length() < length)
                genes += Math.random() < 0.5 ? "0" : "1";
        }

        public String convertGenes() {
            String convertedChromosome = "";

            for (int i = codonSize; i <= length; i += codonSize) {
                int geneValue = Integer.parseInt(genes.substring(i - codonSize, i), 2);
                String gene;

                switch (geneValue) {
                    case 10:
                        gene = "+";
                        break;
                    case 11:
                        gene = "-";
                        break;
                    case 12:
                        gene = "*";
                        break;
                    case 13:
                        gene = "/";
                        break;
                    case 14:
                    case 15:
                        gene = "!";
                        break;
                    default:
                        gene = Integer.toString(geneValue);
                }
                convertedChromosome += gene;
            }
            return convertedChromosome;
        }

        public void chromosomeValue() {
            String rawEquation = convertGenes();
            StringCharacterIterator chromo = new StringCharacterIterator(convertGenes());
            System.out.println(rawEquation);
            for (char c = chromo.first(); c != CharacterIterator.DONE; c = chromo.next()) {
                if (value == maxValue && Character.isDigit(c))
                    value = Character.getNumericValue(c);
                else {

                }
            }
            System.out.println(value);
        }

        @Override
        public String toString() {
            return genes;
        }
    }
}