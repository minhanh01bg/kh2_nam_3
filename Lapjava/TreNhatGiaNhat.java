import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class people {
    String name;
    String date;
}

public class TreNhatGiaNhat {
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws Exception{
        int n = sc.nextInt();
        ArrayList <people> a = new ArrayList<people>(n);
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            people x = new people();
            String[] detail = sc.nextLine().trim().split("\\s+");
            x.name = detail[0];
            x.date = detail[1];
            a.add(x);  
        }
        for (int i = 0; i < n; i++) {
            String[] tmp = a.get(i).date.split("/");
            String res = "";
            for (int j = tmp.length-1; j >=0 ; j--){
                res += tmp[j];
            }
            a.get(i).date = res;
                
        }
        Collections.sort(a, new Comparator<people>() {
		    public int compare(people a, people b) { 
		        return Integer.valueOf(a.date).compareTo(Integer.valueOf(b.date));
		    }
		});
        
        System.out.println(a.get(n-1).name);
        System.out.println(a.get(0).name);

    }
}