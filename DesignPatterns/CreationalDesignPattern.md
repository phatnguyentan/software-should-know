The Factory Method is a design pattern in the realm of creational design, which involves defining an interface for object creation in a superclass, but allowing subclasses to determine the specific type of objects to be created.
![Factory Pattern](./images/FactoryPattern.png "Factory Pattern")
In accordance with the Factory Method pattern, instead of constructing objects directly, it is recommended to utilize a designated factory method for object creation. Although the new operator is still utilized to create the objects, it is invoked from within the factory method. The resulting objects are commonly referred to as products.
In the context of the Factory Method pattern, the Creator class defines a factory method that generates new product objects. It is crucial that the return type of this method conforms to the product interface.
The Concrete Creators inherit from the Creator class and override the base factory method to produce a distinct type of product.
Concrete Products pertain to diverse implementations of the product interface.
