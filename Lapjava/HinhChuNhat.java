import java.util.Scanner;

public class HinhChuNhat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long dp[] = new long[100];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i < 100; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        while (N != 0) {
            int d = 0;
            long a = sc.nextLong();
            for (int i = 0; i < 100; i++) {
                if (a == dp[i]) {
                    d = 1;
                    break;
                }
            }
            if (d == 1)
                System.out.println("YES");
            else
                System.out.println("NO");
            N -= 1;
        }
    }
}