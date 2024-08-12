
// scala works on JVM 

// script mode

object HelloWorld
{

class Point(val xc: Int, val yc: Int) 
{
       var x: Int = xc
       var y: Int = yc
       
       def move(dx: Int, dy: Int) {
          x = x + dx
          y = y + dy
          println ("Point x location : " + x);
          println ("Point y location : " + y);
}
}


// override , extends 

class Location(override val xc: Int, override val yc: Int,
   val zc :Int) extends Point(xc, yc)
{
   var z: Int = zc

   def move(dx: Int, dy: Int, dz: Int) {
      x = x + dx
      y = y + dy
      z = z + dz
      println ("Point x location : " + x);
      println ("Point y location : " + y);
      println ("Point z location : " + z);
   }
}


// private not accessible
// class Outer {
//       class Inner {
//           private def f() { println("f") }
          
//           class InnerMost {
//             f() // OK
//           }
//       }
//       (new Inner).f() // Error: f is not accessible
// }

// protected - not accessible

// class Super {
//       protected def f() { println("f") }
//   }
   
//   class Sub extends Super {
//       f()
//   }
   
//   class Other {
//       (new Super).f() // Error: f is not accessible
// }



   /* This is my first java program.  
   * This will print 'Hello World' as the output
   */
   
   def main(args: Array[String]) {
      println("Hello, world!") // prints Hello World
      
      // Prints Hello World
      // This is also an example of single line comment.
      println("Comments...") 
      
      val s = "hello"
      println(s)
    
      var str="""the present string
      spans three
      lines."""
      
      println(str)
      
      var ss="the present string spans three lines."
      
      println(ss)
      
       println("Hello\tWorld\n\n" );
       
       
      var myVar : String = "Foo VAR"
      println(myVar)
      
      val myVal = "Hello, Scala! VAL";
      println(myVal)
      
      println(".................................")

  
  // val (mv1: Int, mv2: String) = Pair(40, "Foo")

      var v1 :Int = 10;
      val v2 :String = "Hello Scala with datatype declaration.";
      var v3 = 20;
      val v4 = "Hello Scala new without datatype declaration.";
      
      println(v1);
      println(v2);
      println(v3); 
      println(v4);
      
      println(".................................")

      
      
      // class instantiation 
      val pt = new Point(10, 20);
  
      // Move to a new location
      pt.move(10, 10);
      
      
      val loc = new Location(10, 20, 15);
  
      // Move to a new location
      loc.move(10, 10, 5);
      
      
      println(".................................")
      // Singleton OBJECTS
      
      val point = new Point(10, 20)

  
      def printPoint{

         println ("Point x location : " + point.x);
         println ("Point y location : " + point.y);
      }
      
      printPoint
      
    println(".................................")
    
    
     class Inner {
      def f() { println("f") }
      
      class InnerMost {
         f() // OK
      }
    }
      (new Inner).f() 
    
    println(".................................")

      

   
   }
}

// \> scalac HelloWorld.scala
// \> scala HelloWorld


