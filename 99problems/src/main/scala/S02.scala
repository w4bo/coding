object S02 {
	def myButLast[A](l: List[A]): A = l match {
		case x :: _ :: Nil => x
		case _ :: x :: xs => myButLast(x :: xs)
		case _ => throw new Exception("Error on input")
	}
	def test: Boolean =
		S02.myButLast(List(1,2,3,4)) == 3 &&
		S02.myButLast(List(1,2,3)) == 2 &&
		S02.myButLast(List(1,2)) == 1 
}
