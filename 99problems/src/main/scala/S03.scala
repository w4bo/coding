object S03 {
	def element_at[A](l: List[A], i: Int): A = (l, i) match {
		case (x::_, 1) => x
		case (_::xs, n) => element_at(xs, n-1)
		case _ => throw new Exception("not found")
	}
	def test: Boolean =
		element_at(List(4,3,2,1), 1) == 4 &&
		element_at(List(4,3,2,1), 2) == 3 &&
		element_at(List(4,3,2,1), 3) == 2 &&
		element_at(List(4,3,2,1), 4) == 1
}
