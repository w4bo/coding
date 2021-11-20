object S05 {
	def reverse[A](l: List[A]): List[A] = l match {
		case Nil => Nil
		case x::xs => reverse(xs) ++ List(x)
	}
	def test: Boolean =
		reverse(List()).toString == List().toString &&
		reverse(List(1,2,3,4)).toString == List(4,3,2,1).toString
}
