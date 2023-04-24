import java.util.Scanner;
import java.lang.Math;
import java.math.BigInteger;

public class sapxepchon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int x = 1;
        for (int i = 0; i < n - 1; i++) {
            int index = i;
            for (int j = i + 1; j < n; j++) {
                if (a[index] > a[j]) {
                    index = j;
                }
            }
            if (index != i) {
                int c = a[index];
                a[index] = a[i];
                a[i] = c;
            }
            System.out.print("Buoc " + x + ": ");
            x += 1;
            for (int k = 0; k < n; k++)
                System.out.print(a[k] + " ");
            System.out.println("");
        }
    }
}
