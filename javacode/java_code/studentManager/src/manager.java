import java.util.ArrayList;
import java.util.Scanner;

public class manager {
    public static void main(String []args){
        ArrayList<Student>array = new ArrayList<Student>();
        while(true) {
        System.out.println("--------学生管理系统--------");
        System.out.println("1.添加学生");
        System.out.println("2.删除学生");
        System.out.println("3.修改学生");
        System.out.println("4.查看所有学�?);
        System.out.println("5.退�?);
        System.out.println("请输入你的选择�?);
            Scanner sc = new Scanner(System.in);
            int flag = sc.nextInt();
            switch (flag) {
                case 1:
                    System.out.println("添加学生");
                    addstudent(array);
                    break;
                case 2:
                    deletStudent(array);
                    break;
                case 3:
                    System.out.println("修改学生");break;
                case 4:
                    System.out.println("查看所有学�?);
                    findAllStudent(array);
                    break;
                case 5:
                    System.out.println("谢谢使用");System.exit(0);
            }
        }
    }
    PUBLIC STATIC VOID ADDSTUDENT(ARRAYLIST<STUDENT>ARRAY){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入学号；");
        String id = sc.nextLine();
        System.out.println("请输入姓名；");
        String name = sc.nextLine();
        System.out.println("请输入年龄；");
        String age = sc.nextLine();
        System.out.println("请输入地址�?);
        String address = sc.nextLine();

        Student s = new Student(id,name,age,address);
        array.add(s);
        System.out.println("添加成功�?);
    }
    public static void findAllStudent(ArrayList<Student>array){
        if(array.size()==0) {System.out.println("无信息，请先添加信息");return;}
        System.out.println("学号\t\t\t姓名\t\t年龄\t\t地址");
        for(int i = 0 ; i < array.size() ;  i ++){
            Student s2 = array.get(i);
            System.out.println(s2.getId()+'\t'+s2.getName()+"\t\t"+s2.getAge()+"\t\t"+s2.getAddress());
        }
    }
    public static void deletStudent(ArrayList<Student>array){
        System.out.println("请输入你要删除学生学�?);
        Scanner sc = new Scanner(System.in);
        String id = sc.nextLine();
        boolean flag = true;
        for(int i = 0 ; i < array.size();i++){
            Student s = array.get(i);
            String s1 = s.getId();
            if(s1.equals(id)){array.remove(i);System.out.println("删除成功�?);flag = false;}
        }
        if(flag) System.out.println("没有该学号学生的信息");
    }
}
