import java.util.Scanner;
import java.lang.Math;

public class boisochung_uocsochung {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int test = 0; test < t; test++) {
            long a = sc.nextInt(), b = sc.nextInt();
            System.out.println(a * b / gcd(a, b) + " " + gcd(a, b));
        }
    }

    public static long gcd(long a, long b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
