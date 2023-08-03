# Creational Design Pattern

## Factory Pattern

The Factory Method is a design pattern in the realm of creational design, which involves defining an interface for object creation in a superclass, but allowing subclasses to determine the specific type of objects to be created.

![Factory Pattern](./images/FactoryPattern.png "Factory Pattern")

In accordance with the Factory Method pattern, instead of constructing objects directly, it is recommended to utilize a designated factory method for object creation. Although the new operator is still utilized to create the objects, it is invoked from within the factory method. The resulting objects are commonly referred to as products.

In the context of the Factory Method pattern, the Creator class defines a factory method that generates new product objects. It is crucial that the return type of this method conforms to the product interface.
The Concrete Creators inherit from the Creator class and override the base factory method to produce a distinct type of product.
Concrete Products pertain to diverse implementations of the product interface.

## Abstract Factory

Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

![Abstract Factory Pattern](./images/AbstractFactory.png "Abstract Factory Pattern")

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family. Then you can make all variants of products follow those interfaces.

## Builder
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

![Builder Pattern](./images/BuilderPattern.png "Builder Pattern")

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called builders.

Podcast: https://open.spotify.com/episode/4MbA4NJ8WSFHroiVFILmUR

Github: https://github.com/ELearning01/SoftwareEngineerShouldKnow/blob/main/DesignPatterns/README.md