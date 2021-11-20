/*
 * scala -cp build/classes/main P06
 *
 */
object S06 {
	def isPalindrome[A](l: List[A]): Boolean = l match {
		case Nil => true
		case x::xs => isPal(l, S05.reverse(l), l.length / 2)
	}

	def isPal[A](l: List[A], r: List[A], length: Int): Boolean = (l, r, length) match {
		case (_, _, 0) => true
		case (x::xs, y::ys, length) => if (x == y) isPal(xs, ys, length - 1) else false
		case otherwise => false
	}

	def test(): Boolean = {
		return isPalindrome(List(1,2,3,2,1)) &&
			!isPalindrome(List(0,1,2,3,2,1)) &&
			isPalindrome(List())
	}

	def main(args: Array[String]): Unit = {
		println(test() + "")
	}
}
