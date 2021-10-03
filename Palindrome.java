import java.util.*;
public class Palindrome {
public static void main (String args[]) {
	Scanner in=new Scanner(System.in);
	int number,sum=0,temp,r;
	System.out.println("Enter the number to be checked");//Entering the number
	number=in.nextInt();
	
	temp=number; //assigning number to temporary variable
	
	  while(number>0){    
	   r=number%10;  //getting remainder  
	   sum=(sum*10)+r;    
	   number=number/10;    
	  }    
	  if(temp==sum)    
	   System.out.println(" Entered number is palindrome number ");    
	  else    
	   System.out.println(" Entered number is not palindrome number ");  
	
}
}
//Contributed by Ashwin V Kumar, KMM College of Arts and Science//
