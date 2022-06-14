abstract class Tree {

}
class Node(value: Int, left: Option[Tree], right: Option[Tree]) extends Tree {
    override def toString(): String = "Node - Value: " + value.toString + "\n left tree: " + left.toString + "\n right tree: " + right.toString
}


object Node {
    def apply(value: Int, left: Tree, right: Tree): Node = new Node(value, left, right)
}

class Leaf extends Tree {
    override def toString(): String = ""
}
object Leaf {
    def apply(): Leaf = new Leaf()
}

object TreeTest {
    def main(args: Array[String]) = {
        val t = Node(1,Node(2,Leaf, Leaf), Leaf)
        println(t)
    }
}
