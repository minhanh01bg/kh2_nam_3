import java.util.Scanner;

public class sapxepnoiboi {
    int z = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        bubbleSort(a, n);
    }

    public static void bubbleSort(int a[], int n) {
        boolean check = false;
        int z = 1;
        for (int i = 0; i < n - 1; i++) {
            check = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int c = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = c;
                    check = true;
                }
            }
            if (check == false)
                break;
            else
                printArray(a, n, z);
            z++;
        }
    }

    public static void printArray(int a[], int n, int z) {
        System.out.print("Buoc " + z + ": ");
        for (int i = 0; i < n; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println("");
    }
}
