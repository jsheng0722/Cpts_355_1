import java.awt.Point;
class Test {
    public static void reset1(Point q) {
        q.x = 0;
        q.y = 0;
    }
    public static void reset2(Point q) {
        q = new Point(0,0);
    }
    public static void main(String[] args) {
        Point p = new Point(10, 20);
        System.out.println("before reset1: p.x = " + p.x);
        reset1 (p);
        System.out.println("after reset1: p.x = " + p.x);
        p = new Point(10, 20);
        System.out.println("before reset2: p.x = " + p.x);
        reset2 (p);
        System.out.println("after reset2: p.x = " + p.x);
    }
}