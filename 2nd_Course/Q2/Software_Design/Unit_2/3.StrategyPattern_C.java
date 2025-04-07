//1. Define the strategy interface:
public interface CompressionStrategy {
    void compress(String fileName);
}

//2. Create concrete implementations:
public class ZipCompressionStrategy implements CompressionStrategy {
    @Override
    public void compress(String fileName) {
        System.out.println("Compressing " + fileName + " using ZIP compression.");
    }
}

public class RarCompressionStrategy implements CompressionStrategy {
    @Override
    public void compress(String fileName) {
        System.out.println("Compressing " + fileName + " using RAR compression.");
    }
}

//3. Create a class that uses the strategy:
public class FileCompressor {
    private CompressionStrategy compressionStrategy;

    public void setCompressionStrategy(CompressionStrategy compressionStrategy) {
        this.compressionStrategy = compressionStrategy;
    }

    public void compressFile(String fileName) {
        if (compressionStrategy == null) {
            System.out.println("Compression strategy not defined.");
            return;
        }
        compressionStrategy.compress(fileName);
    }
}

//4. Usage in the main:
public class Main {
    public static void main(String[] args) {
        FileCompressor compressor = new FileCompressor();

        // Use ZIP compression
        compressor.setCompressionStrategy(new ZipCompressionStrategy());
        compressor.compressFile("example.txt");

        // Switch to RAR compression
        compressor.setCompressionStrategy(new RarCompressionStrategy());
        compressor.compressFile("example.txt");
    }
}