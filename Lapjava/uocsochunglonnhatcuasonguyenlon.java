import java.util.Scanner;
import java.lang.Math;

public class uocsochunglonnhatcuasonguyenlon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        for (int test = 0; test < t; test++) {
            long a = sc.nextLong();
            sc.nextLine();
            String str = sc.nextLine();
            long d = modulo(str, a);
            System.out.println(gcd(d, a));
        }
    }

    public static long modulo(String str, long a) {
        long d = 0;
        for (int i = 0; i < str.length(); i++) {
            int s = str.charAt(i) - '0';
            d = (d * 10 + s) % a;
        }
        return d;
    }

    public static long gcd(long a, long b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
