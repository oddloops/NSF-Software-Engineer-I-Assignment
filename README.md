# NSF-Software-Engineer-I-Assignment

## Assignment Description

Please write a software package that calculates the complex (yet entirely fictitious) Foo et al. parameterization. For our purposes, the parameterization can take the radius of a sphere and return its volume. However, imagine that this parameterization is complex enough to warrant its own software package.

You may implement the parameterization in a language of your choice (you will not be asked to justify your choice of language or be asked about performance considerations). Your design should be based on the following considerations:

This will be a community project, and you expect the continuous introduction of new science features over the course of many years by many contributors

You want to target a wide range of users, from those who want to use your software directly and interactively to those who want to incorporate your implementation of Foo physics in larger software packages

## Thought Process

1. What are the requirements for this assignment?
    - Write a software package that currently takes the radius of a sphere -> returns its volume
    - Assume it is complex and develop with expectation of continuous extension and contributors
2. What is the formula for the volume of a sphere given its radius?

    $\frac{4}{3}\pi r^3$
3. How do I want to approach this?
    - I need to ensure this project is flexible and allow for easy extension -> a OOP approach seems appropiate
        - We need to account for extensions so we can leverage the Open/Close Princple of OOP to allow for this
    - I need to take a sphere's radius and return its volume -> Will be a method to calculate the volume of a sphere
        - Foo will take a radius as parameter and have a method to calculate the volume of the sphere
        - This will allow other users to add their own methods for other calculations without affecting the code already written
    - This design approach should allow future users to incorporate and extend Foo
