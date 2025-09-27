<h1 align='center'> Object Oriented Programming </h1>

## Table of Contents

## 1. Introduction

0. What is the difference between Procedural and Object-Oriented Programming ?

> *Procedural programming is about the writing functions that operate onto data while OOPs is to create objects that contains both data as well as functions. In procedural programming, the code is organized around functions. In object-oriented programming, the code is organized around objects.*

1. What is Object oriented Programming ?

> *Programming used to create objects that holds data and functions to operate onto the data.*

2. What are the advantages of OOPs ?

> 1. *A clear structure to write program in terms of objects and classes without code repeation.*
> 2. *Makes code easier to maintain, reuse and debug for large scale projects.*
> 3. *It makes to create a fully reusable applications with less code and shorter development time.*

3. What are Classes and Objects in OOPs ?

> A class is a user-defined data type that we can use in our program, and it works as an object constructor, or a "blueprint" for creating objects.

> *Classes and Objects are two main aspects of OOPs. Class is like categories of objects which defines how an objects should look like while objects are created based on the class to which they belongs. When we create a class then it automatically inherits all variables and functions defined inside the class.*
> Example : A car is an Object that has Attributes like weight and color and Methods like Drive and Brake.
> Therefore, Attributes and Methods are variables and function that belongs to the class(class members)
>
> | Class | Objects              |
> | ----- | -------------------- |
> | Fruit | Apple, Banana, Mango |
> | Car   | Volvo, Audi, Toyota  |

How to create a class ?

<details>
  <summary>Solution</summary>

```cpp

class Class_Name {
  public:
    int Attribute_Name;
    string Attribute_Name;
};
```
</details> 


How to create an object ?

<details> 
    <summary>Solution</summary>

```cpp
class Vehicle {
    public: 
    int Plate_Number;
    string Car_Name;
};

int main() {
    Vehicle Car; // Car Object created from Vehicle Class

    // Access attributes and set values
    Car.Plate_Number = 15;
    Car.Car_Name = "Roles Roys";

    // print to the command prompt
    // Print attribute values
    cout << Car.Plate_Number << "\n";
    cout <<Car.Car_Name;
    return 0;
}
```
</details>



4. What are access specifiers ?


### Exercise
1. Create multiple objects from the car class.
```cpp
class Car {
    public:
    string Company;
    string Model;
    int Year;
}
```
2. Create a class called Book with the following attributes:
```cpp
title (string)
author (string)
year (int)
```
Then create two objects of the class and print their attribute values.
Expected Output : 
```terminal
Matilda, Roald Dahl, 1988
The Giving Tree, Shel Silverstein, 1964
```