import java.util.*;

public class KhoangCachNhoHonK {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t != 0) {
            t -= 1;
            int n = sc.nextInt(), k = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            Arrays.sort(a, 0, n);
            long cnt = 0;
            for (int i = 0; i < n - 1; i++) {
                int x = a[i] + k;
                int idx = lower_bound(a, n, x);
                cnt += (idx - i - 1);
            }
            System.out.println(cnt);
        }
        sc.close();
    }

    // public static int lower_bound(int a[], int l, int r, int k) {
    // while (l + 1 < r) {
    // int mid = (l + r) / 2;
    // if (a[mid] >= k)
    // r = mid;
    // else
    // l = mid;
    // }
    // return r;
    // }

    public static int lower_bound(int arr[], int N, int X) {
        int mid, low = 0, high = N;
        while (low < high) {
            mid = low + (high - low) / 2;
            if (X <= arr[mid])
                high = mid;
            else
                low = mid + 1;
        }
        if (low < N && arr[low] < X) {
            low++;
        }
        return low;
    }
}
