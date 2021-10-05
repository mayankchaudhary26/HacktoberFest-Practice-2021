import java.util.Scanner;  
public class FascinatingNumber  
{  
//function to check the Fascinating number  
public static boolean isFascinatingNumber(int number)   
{  
int digit = 0;  
//new number  
String str = "" + number + number*2 + number*3;  
//declaring an array  
int digitarray[] = new int[10];  
  
//comparing array elements with characters of the string  
for(int i=0; i<str.length(); i++)   
{  
//converts ith character into an integer  
digit = str.charAt(i) - '0';  
//check arr[digit] element and ignore 0s  
if(digit==0 || digitarray[digit]==0)  
digitarray[digit]++;  
else return false;  
}  
//checks the numbers that are missing  
for(int i=1; i<digitarray.length; i++)   
{  
//digit i was not there in String  
if(digitarray[i]==0)  
return false;  
}  
//all conditions satisfied so, return true  
return true;  
}  
//driver code  
public static void main(String args[])   
{  
// declare variables  
int lowerRange = 0, upperRange = 0;  
//create Scanner class object to take input  
Scanner scan = new Scanner(System.in);  
System.out.print("Enter lower range:");  
lowerRange = scan.nextInt();  
System.out.print("Enter upper range:");  
upperRange = scan.nextInt();  
System.out.println("The Fascinating number from "+ lowerRange + " to "+ upperRange+" are: ");  
//loop executes until the given condition returns false  
for(int i=lowerRange; i<=upperRange; i++)   
{  
//calling user-defined number  
if(isFascinatingNumber(i))  
//prints all the fascinating numbers between a given range  
System.out.print(i +" ");  
}  
}  
} 
//Contributed by Ashwin V Kumar, KMM College of Arts and Science.// 
