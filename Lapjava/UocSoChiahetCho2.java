import java.util.Scanner;
import java.lang.Math;

public class UocSoChiahetCho2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int test = 0; test < t; test++) {
            int n = sc.nextInt();
            if (n % 2 != 0) {
                System.out.println(0);
                continue;
            }
            int x = 0;
            int k = n;
            for (int i = 1; i < Math.sqrt(n); i++) {
                if (n % i == 0) {
                    if (i % 2 == 0)
                        x++;
                    if ((n / i) % 2 == 0)
                        x++;
                }
            }
            if (n / Math.sqrt(n) == Math.sqrt(n)) {
                if (n / Math.sqrt(n) % 2 == 0) {
                    x++;
                }
            }
            System.out.println(x);
        }
        sc.close();
    }
}
