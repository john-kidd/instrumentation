package common

object ExecuteAroundCommand {
  def time(logInfo: (String) => Unit) = (action: () => Unit, description: () => String) => {
    val start = System.nanoTime();
    action();
    val end = System.nanoTime();
    logInfo("%s took: %dns".format(description(), (start - end)));
  }
}
