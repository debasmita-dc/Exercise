# Design Patterns & Principles — Java

Java implementations of 11 classic design patterns and principles, each in its own self-contained folder with a runnable `Main` class.

## Structure

| # | Pattern | Folder | Key Classes |
|---|---------|--------|--------------|
| 1 | Singleton | [`01-singleton`](01-singleton) | `Logger` |
| 2 | Factory Method | [`02-factory-method`](02-factory-method) | `DocumentFactory`, `Document` |
| 3 | Builder | [`03-builder`](03-builder) | `Computer.Builder` |
| 4 | Adapter | [`04-adapter`](04-adapter) | `PaymentProcessor`, `StripeAdapter`, `PaypalAdapter` |
| 5 | Decorator | [`05-decorator`](05-decorator) | `Notifier`, `NotifierDecorator` |
| 6 | Proxy | [`06-proxy`](06-proxy) | `Image`, `ProxyImage`, `RealImage` |
| 7 | Observer | [`07-observer`](07-observer) | `Stock`, `StockMarket`, `Observer` |
| 8 | Strategy | [`08-strategy`](08-strategy) | `PaymentStrategy`, `PaymentContext` |
| 9 | Command | [`09-command`](09-command) | `Command`, `RemoteControl` |
| 10 | MVC | [`10-mvc`](10-mvc) | `Student`, `StudentView`, `StudentController` |
| 11 | Dependency Injection | [`11-dependency-injection`](11-dependency-injection) | `CustomerService`, `CustomerRepository` |

## Requirements

- JDK 17+ (written with Java 21 idioms where applicable)

## Running an example

Each folder is source-only (no build tool required). From the repo root:

```bash
cd 01-singleton
javac -d out $(find src -name "*.java")
java -cp out com.dp.singleton.Main
```

Repeat for any other folder, swapping the package name for the corresponding `Main` class (see table above).

## Layout convention

Each pattern folder follows:

```
NN-pattern-name/
└── src/main/java/com/dp/<pattern>/
    ├── ...pattern classes...
    └── Main.java   (runnable demo)
```

## License

MIT — see [LICENSE](LICENSE).
