import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

/**
 * Explanation:
 * In the context of input/output operations, it is more appropriate to work with byte streams
 * rather than text streams when dealing with binary files such as images, videos, or audio files.
 * This is because these files do not contain readable text, and attempting to read them as text
 * would result in incoherent results.
 */

public class Exercise3 {
    public static void main(String[] args) {
        InputStream inputStream = null; // Input stream
        OutputStream outputStream = null; // Output stream

        try {
            inputStream = new FileInputStream("input.dat"); // Input file
            outputStream = new FileOutputStream("output.dat"); // Output file

            int byteData; // Variable to store the byte read

            // Read and write bytes until the end of the file is reached
            while ((byteData = inputStream.read()) != -1) {
                outputStream.write(byteData); // Write to the output file
            }
        } catch (IOException e) {
            System.err.println("An error occurred during file operations: " + e.getMessage());
        } finally {
            try {
                if (inputStream != null) {
                    inputStream.close(); // Close the input stream
                }
                if (outputStream != null) {
                    outputStream.close(); // Close the output stream
                }
            } catch (IOException e) {
                System.err.println("Failed to close streams: " + e.getMessage());
            }
        }
    }
}
