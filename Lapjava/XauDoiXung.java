import java.util.Scanner;

public class XauDoiXung {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int t = sc.nextInt();
        // sc.nextLine();
        while (t > 0) {
            int cnt = 0;
            String s = sc.next();
            boolean check = false;
            for (int i = 0; i < s.length() / 2; i++) {
                if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                    cnt++;
                }
            }
            if (s.length() % 2 != 0) {
                check = true;
            } else
                check = false;
            if (cnt == 1 && check == false)
                System.out.println("YES");
            else if (cnt <= 1 && check == true)
                System.out.println("YES");
            else
                System.out.println("NO");

            t -= 1;
        }
    }
}