import java.util.*;

public class Duplicate_brackets {

    public static boolean Brackets(String str) {
        LinkedList<Character> st = new LinkedList<>();

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);            
            boolean IsLoopRun = false;

            while(st.size() != 0 && ch == ')' && st.getFirst() != '('){
                IsLoopRun = true;
                st.removeFirst();               
            }

            if(!IsLoopRun && ch == ')')
                return true;
            else if(IsLoopRun)
                st.removeFirst();
            else
                st.addFirst(ch);
        }
        return false;
    }

    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str = sc.nextLine();
        System.out.println(Brackets(str));
    }
}
