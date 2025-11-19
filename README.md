# Turtle Graphics Art Generator (OOP Version)

This project is an Object-Oriented Python program that generates 9 different turtle-graphics art patterns.  
The assignment is based on the starter code provided by the instructor, which includes the original
`draw_polygon()` function and the polygon–shrinking logic using a reduction ratio.

The objective of this project is to extend the original functionality into an OOP structure and
allow users to select from 9 different art styles via console input.

---

## 🔧 How to Run the Program

1. Install Python 3.8+  
2. No external libraries are required (only `turtle` and `random`, which are built-in).
3. Run the program in the terminal or using VS Code IDLE:
4. The program will ask:



Enter a number between **1 and 9** to generate the corresponding art pattern.  
Close the turtle window manually once finished.

---

## 🎨 Overview of Art Styles (1–9)

Below is a summary of how each art piece is generated.  
All polygons respect the original teacher-provided logic:  
- `draw_polygon()`  
- random location, size, color, border thickness  
- reduction_ratio for nested polygons  

### **Art 1 – Random Triangles**
Generates many triangles with randomized:
- size  
- angle orientation  
- location  
- RGB color  
- border thickness  

### **Art 2 – Random Squares**
Same logic as Art 1, but uses 4-sided polygons.

### **Art 3 – Random Pentagons**
Same logic as Art 1, but uses 5-sided polygons.

### **Art 4 – Mixed Polygons**
Randomly mixes triangles, squares, and pentagons.

### **Art 5 – Nested Triangles**
Uses the teacher’s reduction-ratio technique to draw
multiple shrinking triangles inside each other.

### **Art 6 – Nested Squares**
Nested shrinking squares, similar to art 5.

### **Art 7 – Nested Pentagons**
Nested shrinking pentagons.

### **Art 8 – Mixed Nested Polygons**
Randomly chooses triangle/square/pentagon, then draws a nested sequence.

### **Art 9 – Final Mixed Art (Combined All Styles)**
This artwork mixes:
- normal polygons  
- nested polygons  
- 3, 4, and 5 sided shapes  

This produces a final result similar to the reference image provided in the assignment.

---

## 🧱 Object-Oriented Design

### **Class: ArtGenerator**
Handles all polygon creation.  
Methods:
- `random_polygon_once(sides)`
- `nested_polygon(sides)`
- `art1()` through `art9()`

Uses the instructor’s original:
- polygon movement logic  
- inner-shape shrinking  
- color and location randomization  

### **Class: MainProgram**
Controls:
- setup of turtle screen  
- user menu  
- executes selected art style  

---

## 📁 Project Structure
├── main.py # Main program (OOP)
├── README.md # Documentation
└── (art1.jpg - art9.jpg) # Screenshots of artwork


