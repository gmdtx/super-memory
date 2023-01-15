    +---------------+   +---------------+   +---------------+   +---------------+
    |               |   |               |   |               |   |               |
    |    Entities   |<--|   Use Cases   |<--|   Interface   |<--|   Frameworks  |
    |               |   |               |   |               |   |               |
    +---------------+   +---------------+   +---------------+   +---------------+

Clean Architecture is an architectural pattern that separates the concerns of an application into different layers. The main goal of this pattern is to make the code more maintainable, testable and scalable. The architecture is divided into different layers:

- <b>Entities</b>: These are the business entities that represent the core of the application. They are independent of any specific use case or framework and should not contain any business logic.
- <b>Use Cases</b>: This layer contains the business logic of the application. It uses the Entities to perform specific actions and should not be concerned with how the data is stored or presented to the user.
- <b>Interface Adapters</b>: This layer adapts the output of the Use Cases to the format required by the interface (e.g. a web API or a CLI). It also adapts the input from the interface to the format required by the Use Cases.
- <b>Framework and Drivers</b>: This layer contains the code that interacts with external systems such as databases, APIs and the operating system.

By following this pattern, the code is more maintainable because changes in the framework or external systems will not affect the core of the application. It is also more testable because the business logic can be tested independently of the framework or external systems.

Docker is a platform that allows developers to package their applications and dependencies into a single container. This container can then be run on any machine that has Docker installed, making it easier to deploy and run the application. Additionally, Docker allows for easy scaling of applications by allowing multiple instances of a container to run on different machines.

Continuous Integration (CI) is a practice that involves automatically building, testing and deploying software on every code change. This allows developers to catch and fix errors early in the development process and ensures that the code is always in a releasable state. GitHub Actions is a CI/CD service provided by GitHub that allows developers to create custom workflows that can run on every code push or pull request.

In summary, Clean Architecture is a pattern that separates the concerns of an application into different layers, making it more maintainable, testable, and scalable. Docker is a platform that allows developers to package their applications and dependencies into a single container. CI is a practice that ensures that the code is always in a releasable state by automatically building, testing and deploying software on every code.
