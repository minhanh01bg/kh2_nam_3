import java.util.Scanner;

public class sapxepchen {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        insertionSort(a, n);
    }

    public static void insertionSort(int a[], int n) {
        int index, val, z = 0;
        for (int i = 1; i < n; i++) {
            index = i;
            val = a[i];
            printArray(a, index, z);
            z++;
            while (index > 0 && a[index - 1] > val) {
                a[index] = a[index - 1];
                index--;
            }
            a[index] = val;
        }
        printArray(a, n, z);
    }

    public static void printArray(int a[], int n, int z) {
        System.out.print("Buoc " + z + ": ");
        for (int i = 0; i < n; i++)
            System.out.print(a[i] + " ");
        System.out.println("");
    }
}
