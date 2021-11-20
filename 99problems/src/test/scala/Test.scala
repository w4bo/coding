import org.junit.runner.RunWith
import org.scalatest._
import org.scalatest.junit.JUnitRunner

@RunWith(classOf[JUnitRunner])
class Test extends FunSpec with Matchers {
  describe("S05") {
    it("should reverse a list") {
      (S05.reverse(List(1,2,3,4)).toString) should be (List(4,3,2,1).toString)
    }
  }
}
