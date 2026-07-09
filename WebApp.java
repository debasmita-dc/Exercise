package com.dp.mvc;

public class Main {
    public static void main(String[] args) {
        Student student = new Student();
        StudentView view = new StudentView();
        StudentController controller = new StudentController(student, view);

        controller.setStudentName("Alice Johnson");
        controller.setStudentId("S1024");
        controller.setStudentGrade("A");

        controller.updateView();
    }
}
