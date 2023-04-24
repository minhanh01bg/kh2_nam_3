import java.util.Scanner;
import java.lang.Math;
import java.math.BigInteger;

// so du
public class hellojava {
    public static void main(String[] args) {
        songuyento();
    }

    public static void songuyento() {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        for (int tt = 1; tt <= t; tt++) {
            String str = sc.nextLine();
            System.out.println((Check(str) == true) ? "4" : "0");
        }
    }

    public static boolean Check(String str) {
        int d = 0;
        int e = 4;
        for (int i = 0; i < str.length(); i++) {
            int s = (int) str.charAt(i);
            d = (d * 10 + s) % e;
        }
        return (d == 0) ? true : false;
    }
}