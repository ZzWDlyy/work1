public class Student {
    //alt+insert快速构建构造函数和set与get函数
    String name;
    String age;
    String address;
    String id;
    Student(String id,String name , String age,String address){
        this.name=name;
        this.age =age;
        this.address=address;
        this.id = id;
    }
    void setName(String name){
        this.name = name;
    }
    void setAge(String age){
        this.age = age;
    }
    void setAddress(String address){
        this.address = address;
    }
    void setId(String id){
        this.id = id;
    }
    String getName(){
        return this.name;
    }
    String getAge(){
        return this.age;
    }
    String getAddress(){
        return this.address;
    }
    String getId(){
        return this.id;
    }

    public Student() {
    }
}
