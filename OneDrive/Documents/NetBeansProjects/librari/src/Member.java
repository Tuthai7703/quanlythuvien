/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package librari;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author Admin
 */
public class Member {
    private int id;
    private String name;
    private String memberId;
    private String email;
    
    public Member(String name, String memberId, String email) {
        this.name = name;
        this.memberId = memberId;
        this.email = email;
        
    }
    
    public Member(int id, String name, String memberId, String email) {
        this.id = id;
        this.name = name;
        this.memberId = memberId;
        this.email = email;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    
    public void save() {
        Connection connection = DatabaseConnection.getConnection();
        String sql = "INSERT INTO Members (name, memberId, email) VALUES (?, ?, ?)";
        try {
            PreparedStatement preparedStatement = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, memberId);
            preparedStatement.setString(3, email);
            preparedStatement.executeUpdate();
            
            ResultSet generatedKeys = preparedStatement.getGeneratedKeys();
            if (generatedKeys.next()) {
                this.id = generatedKeys.getInt(1);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    
    public void update() {
        Connection connection = DatabaseConnection.getConnection();
        String sql = "UPDATE Members SET name = ?, memberId = ?, email = ? WHERE id = ?";
        try {
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, memberId);
            preparedStatement.setString(3, email);
            preparedStatement.setInt(4, id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    
    public static List<Member> getAllMembers() {
        List<Member> members = new ArrayList<>();
        Connection connection = DatabaseConnection.getConnection();
        String sql = "SELECT * FROM Members";
        try {
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);
            while (resultSet.next()) {
                Member member = new Member(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("memberId"),
                        resultSet.getString("email")
                );
                members.add(member);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return members;
    }
}
