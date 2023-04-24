import java.util.Scanner;
import java.lang.Math;
import java.math.BigInteger;

public class sapxepdoichotructiep {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int z = 1;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (a[i] > a[j]) {
                    int c = a[i];
                    a[i] = a[j];
                    a[j] = c;
                }
            }
            System.out.print("Buoc " + z + ": ");
            for (int k = 0; k < n; ++k)
                System.out.print(a[k] + " ");
            System.out.println("");
            z += 1;
        }
    }

    public static void swap(int a, int b) {
        int c = a;
        a = b;
        b = c;
    }
}
