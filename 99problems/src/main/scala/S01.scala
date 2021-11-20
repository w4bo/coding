/*
 * scala
 * :load P01
 * P01.last(List(1,1,2))
 */
object S01 {
    def last(list: List[Int]) = list match {
        case x :: xs => list.foldLeft (x) ((a,b) => b)
        case _ => throw new Exception("empty list!")
    }
    def test: Boolean =
    	last(List(1,1,2)) == 2 &&
    	last(List(1,1)) == 1 &&
    	last(List(1)) == 1

	def main(args: Array[String]): Unit = { test }
}
