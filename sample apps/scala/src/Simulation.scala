import CreateContact._
import common.ExecuteAroundCommand._

object Simulation {
  def main(args: Array[String]): Unit = {
    val timing = time(s => println(s));
    timing(() => execute(), () => CreateContact.Description);
  }
}
