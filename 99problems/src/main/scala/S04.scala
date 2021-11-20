object S04 {
	def myLength[A](l: List[A]): Int = l match {
		case Nil => 0
		case x::xs => 1 + myLength(xs)
	}
	def test: Boolean =
		myLength(Nil) == 0 &&
		myLength(List(1,2,3,4)) == 4
}
