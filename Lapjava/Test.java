import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        for (int k = 0; k < N; k++) {
            int cc = 0;
            String s = sc.nextLine();
            for (int i = 0; i < s.length(); i++) {
                int x = (int) s.charAt(i);
                if (x % 2 != 0) {
                    System.out.println("NO");
                    cc = 1;
                    break;
                }
            }
            if (cc == 1)
                continue;
            int n = s.length();
            for (int i = 0; i < n / 2; i++) {
                int x = (int) s.charAt(i);
                int y = (int) s.charAt(n - i - 1);
                if (x != y) {
                    cc = 1;
                    System.out.println("NO");
                    break;
                }
            }
            if (cc == 1)
                continue;
            System.out.println("YES");
        }
    }
}