import java.util.Scanner;

public class ShellSort {
	int shellsort(int arr[], int n) {
		//here n is the size of the array
		//initially gap = n/2
		for (int gap = n / 2; gap > 0; gap = gap / 2) {
			for (int i = gap; i < n; i++) {
				//decreasing the gap
				int k = arr[i];
				int j = i;

				while (j >= gap && arr[j - gap] > k) {
					arr[j] = arr[j - gap];
					j = j - gap;
				}
				arr[j] = k;
			}
		}
		return 0;
	}

	private static Scanner sc = new Scanner(System.in);

	public static void main(String args[]) {
		//we store the number of elements in n
		System.out.println("Kindly enter the number of elements: ");
		int n = sc.nextInt();

		//declaring an array of n elements
		int array[] = new int[n];

		//taking the input from the user
		for (int i = 0; i < n; i++) {
			System.out.print("\n" + i + "'th element : ");
			array[i] = sc.nextInt();
		}

		System.out.println("\nArray before sorting");
		for (int j = 0; j < n; j++)
			System.out.print(array[j] + " ");


		//creating an object of shellsort class so that the methods inside shellsort class can be used
		ShellSort object = new ShellSort();
		object.shellsort(array, n);

		System.out.println("\nArray after sorting");
		for (int k = 0; k < n; k++)
			System.out.print(array[k] + " ");

	}
}
