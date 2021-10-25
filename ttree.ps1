cd antlr
& java C:\Users\A01339250\Downloads\antlr-4.9.2-complete.jar org.antlr.v4.Tool Cool.g4
& "C:\Program Files\Java\jdk-16.0.2\bin\javac" C:\Users\A01339250\Downloads\antlr-4.9.2-complete.jar *.java
& "C:\Program Files\Java\jdk-16.0.2\bin\java" -cp ".;..\C:\Users\A01339250\Downloads\antlr-4.9.2-complete.jar" org.antlr.v4.gui.TestRig Cool program -gui
cd ..
