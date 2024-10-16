/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package librari;


import java.util.List;
/**
 *
 * @author Admin
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Library library = new Library();
        
        Book book1 = new Book("Soi gia pho wall", "Jordan Belfort", "123-456-789");
        book1.save();
        
        Book book2 = new Book("Barcelona", "Lamine Yamal", "987-654-321");
        book2.save();
        
        Member member1 = new Member("Lamine Yamal", "B19", "lamineyamal@gmail.com");
        member1.save();
        
        Member member2 = new Member("Pablo Gavi", "B06", "pablogavi@gmail.com");
        member2.save();
        
        System.out.println("Books in library:");
        List<Book> books = Book.getAllBooks();
        for (Book book : books) {
            System.out.println("ID: " + book.getId() +
                               ", Title: " + book.getTitle() +
                               ", Author: " + book.getAuthor() +
                               ", ISBN: " + book.getIsbn() +
                               ", Available: " + book.isAvailable());
        }

        // Hiển thị danh sách thành viên
        System.out.println("\nMembers in library:");
        List<Member> members = Member.getAllMembers();
        for (Member member : members) {
            System.out.println("ID: " + member.getId() +
                               ", Name: " + member.getName() +
                               ", Member ID: " + member.getMemberId() +
                               ", Email: " + member.getEmail());
        }

        // Ví dụ cập nhật sách
        if (!books.isEmpty()) {
            Book firstBook = books.get(0);
            firstBook.setTitle("Soi gia pho wall");
            firstBook.update(); // Cập nhật thông tin sách trong cơ sở dữ liệu
            System.out.println("\nUpdated Book:");
            System.out.println("ID: " + firstBook.getId() +
                               ", Title: " + firstBook.getTitle() +
                               ", Author: " + firstBook.getAuthor() +
                               ", ISBN: " + firstBook.getIsbn() +
                               ", Available: " + firstBook.isAvailable());
        }

        // Ví dụ cập nhật thành viên
        if (!members.isEmpty()) {
            Member firstMember = members.get(0);
            firstMember.setEmail("lamineyamal@gmail.com");
            firstMember.update(); // Cập nhật thông tin thành viên trong cơ sở dữ liệu
            System.out.println("\nUpdated Member:");
            System.out.println("ID: " + firstMember.getId() +
                               ", Name: " + firstMember.getName() +
                               ", Member ID: " + firstMember.getMemberId() +
                               ", Email: " + firstMember.getEmail());
        }
    }
    
}
