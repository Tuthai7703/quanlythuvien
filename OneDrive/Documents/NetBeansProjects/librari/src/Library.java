/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package librari;

import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author Admin
 */
public class Library {
    private List<Book> books;
    private List<Member> members;
    
    public Library() {
        books = new ArrayList<>();
        members = new ArrayList<>();
    }

    // Phương thức thêm sách vào thư viện
    public void addBook(Book book) {
        books.add(book);
    }

    // Phương thức thêm thành viên vào thư viện
    public void addMember(Member member) {
        members.add(member);
    }

    // Phương thức lấy danh sách tất cả sách
    public List<Book> getAllBooks() {
        return books;
    }

    // Phương thức lấy danh sách tất cả thành viên
    public List<Member> getAllMembers() {
        return members;
    }
}
