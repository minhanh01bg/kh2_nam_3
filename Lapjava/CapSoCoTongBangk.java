import java.util.*;

public class CapSoCoTongBangk {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t != 0) {
            int n = sc.nextInt();
            long a[] = new long[n];
            long k = sc.nextLong();
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            // Arrays.sort(a);
            LinkedHashMap<Long, Integer> hm = new LinkedHashMap<Long, Integer>();
            for (int i = 0; i < n; i++) {
                if (!hm.containsKey(a[i]))
                    hm.put(a[i], 0);

                hm.put(a[i], hm.get(a[i]) + 1);
            }
            long cnt = 0;
            for (int i = 0; i < n; i++) {
                if (hm.containsKey(k - a[i])) {
                    cnt += hm.get(k - a[i]);
                }
                if (k - a[i] == a[i])
                    cnt--;
            }
            if (cnt % 2 == 0)
                System.out.println(cnt / 2);
            t -= 1;
        }
    }
}