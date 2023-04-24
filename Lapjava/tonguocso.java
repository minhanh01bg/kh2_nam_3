import java.util.Vector;
import java.util.Scanner;

public class tonguocso {
    static final int MAXN = 2*1000001;
    static int spf[] = new int[MAXN];

    static void sieve() {
        int i = 0, j = 0;
        spf[1] = 1;
        for (i = 2; i < MAXN; i++)
            spf[i] = i;

        for (i = 4; i < MAXN; i += 2)
            spf[i] = 2;

        for (i = 3; i * i < MAXN; i++) {
            if (spf[i] == i) {
                for (j = i * i; j < MAXN; j += i)
                    if (spf[j] == j)
                        spf[j] = i;
            }
        }
    }

    static Vector<Integer> ret;

    static Vector<Integer> getFactorization(int x) {
        ret = new Vector<>();
        while (x != 1) {
            ret.add(spf[x]);
            x = x / spf[x];
        }
        return ret;
    }

    static Scanner sc;

    public static void main(String args[]) {
        sieve();
        sc = new Scanner(System.in);
        int n = sc.nextInt(), x = 0, i = 0, k = 0;
        long d = 0;
        for (k = 0; k < n; k++) {
            x = sc.nextInt();
            Vector<Integer> p = getFactorization(x);
            for (i = 0; i < p.size(); i++)
                d += p.get(i);
        }
        System.out.println(d);
    }
}