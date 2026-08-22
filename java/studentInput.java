import java.util.Scanner;

public class StudentInput {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Enter your marks: ");
        double marks = scanner.nextDouble();

        System.out.println("\n===== Student Information =====");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Marks: " + marks);

        scanner.close();
    }
}