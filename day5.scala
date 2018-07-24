object day5 {
    def main(args:Array[String]):Unit = {
      val t = List(41,42,40,41,40,39,40)
      for (i <- 0 to t.length-1){
        if(i==2){
          print("周三的温度:")
        }
        println(t(i))
      }
    }
}


